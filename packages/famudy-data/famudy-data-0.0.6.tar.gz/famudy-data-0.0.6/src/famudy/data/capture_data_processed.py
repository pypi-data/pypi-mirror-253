import os.path
import os.path
import re
from pathlib import Path
from typing import List, Iterator, Any, Tuple, Union

from famudy.config.run.calibration import CalibrationResult, CalibrationRunConfig
from famudy.config.run.calibration_params import IntrinsicParams

try:
    from typing import Literal
except ImportError:
    # Python 3.7 doesn't have Literal
    from typing_extensions import Literal

import trimesh
from PIL import Image
import numpy as np
import open3d as o3d
from elias.folder import DataFolder
from elias.manager import BaseDataManager
from elias.util import load_img, load_json, ensure_directory_exists, ensure_directory_exists_for_file, \
    save_img

from famudy.env_data import FAMUDY_PROCESSED_CAPTURE_DATA_PATH, FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH
from dreifus.matrix import Intrinsics, Pose

FrameRateType = Literal['24fps', '73fps']


# TODO: default FrameRate should be 73fps for everything

class ProcessedCaptureDataManager(BaseDataManager[None, None, None]):

    def __init__(self,
                 participant_id: int,
                 create_if_not_exists: bool = False,
                 remote: bool = False):
        processed_capture_data_path = FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH if remote else FAMUDY_PROCESSED_CAPTURE_DATA_PATH
        if create_if_not_exists:
            ensure_directory_exists(f"{processed_capture_data_path}/{participant_id:03d}")
        super(ProcessedCaptureDataManager, self).__init__(processed_capture_data_path,
                                                          f"{participant_id:03d}",
                                                          None)

        self._participant_id = participant_id
        self._calibration_run_config = None

        self.valid_landmark_detectors = ['PIPnet', 'HRNet', 'pips']
        if Path(self.get_calibration_run_config_path()).exists():
            self.serials = self.load_calibration_run_config().serials

            self._lms2D = {detector: {serial: None for serial in self.serials} for detector in
                           self.valid_landmark_detectors}
            self._lms3D = {detector: {serial: None for serial in self.serials} for detector in
                           self.valid_landmark_detectors}
            self._bboxes = {serial: None for serial in self.serials}

            self._color_corrections = {serial: None for serial in self.serials}

    def load_image(self,
                   sequence: str,
                   serial: str,
                   timestep: int,
                   downscale_factor: int = 1,
                   framerate: FrameRateType = '24fps',
                   use_color_correction: bool = False,
                   use_robust_matting_mask: bool = False) -> np.ndarray:
        image = load_img(self.get_image_path(sequence,
                                             serial,
                                             timestep,
                                             downsample_factor=downscale_factor,
                                             framerate=framerate))

        if use_color_correction:
            image = image / 255.  # Cast to float
            affine_color_transform = np.load(self.get_color_correction_path(sequence, serial))
            image = image @ affine_color_transform[:3, :3] + affine_color_transform[np.newaxis, :3, 3]
            image = np.clip(image, 0, 1)
            image = (image * 255).astype(np.uint8)

        if use_robust_matting_mask:
            cam_id = self.serials.index(serial)
            mask = self.load_robust_matting_alpha_image(sequence, timestep, cam_id, framerate=framerate)

            mask = Image.fromarray(mask)
            mask = mask.resize((image.shape[1], image.shape[0]), resample=Image.BILINEAR)
            mask = np.asarray(mask, dtype="uint8")
            mask = np.expand_dims(mask, axis=2)

            image = image / 255.
            mask = mask / 255.
            image = mask * image + (1 - mask) * np.ones_like(image)

            image = image * 255.
            image = np.clip(image, 0, 255)
            image = image.astype(np.uint8)

        return image

    def load_masked_image(self,
                          sequence: str,
                          cam_id: int,
                          timestep: int,
                          downscale_factor: int = 1,
                          framerate: FrameRateType = '24fps'
                          ) -> np.ndarray:
        serial = self.load_calibration_run_config().serials[cam_id]
        image = self.load_image(sequence, serial, timestep, downscale_factor=downscale_factor, framerate=framerate)
        mask = self.load_robust_matting_alpha_image(sequence, timestep, cam_id, framerate=framerate)

        mask = Image.fromarray(mask)
        mask = mask.resize((image.shape[1], image.shape[0]), resample=Image.BILINEAR)
        mask = np.asarray(mask, dtype="uint8")
        mask = np.expand_dims(mask, axis=2)

        image = image / 255.
        mask = mask / 255.
        image = mask * image + (1 - mask) * np.ones_like(image)

        image = image * 255.
        image = np.clip(image, 0, 255)
        image = image.astype(np.uint8)

        return image

        # if self._dataparser_outputs.alpha_channel_filenames is not None:
        #     alpha_channel_filename = self._dataparser_outputs.alpha_channel_filenames[image_idx]
        #     pil_alpha_image = Image.open(alpha_channel_filename)
        #     pil_alpha_image = pil_alpha_image.resize(pil_image.size, resample=Image.BILINEAR)
        #
        #     alpha_image = np.asarray(pil_alpha_image, dtype="uint8")
        #     image = np.concatenate([image, alpha_image[..., None]], axis=-1)

    def load_masked_image_color_corrected(self,
                                          sequence: str,
                                          cam_id: int,
                                          timestep: int,
                                          downscale_factor: int = 1,
                                          framerate: FrameRateType = '24fps'
                                          ) -> np.ndarray:
        serial = self.load_calibration_run_config().serials[cam_id]
        image = self.load_image(sequence, serial, timestep, downscale_factor=downscale_factor, framerate=framerate)
        color_transform = self.load_affine_color_correction(sequence_name=sequence, serial=self.serials[cam_id])
        mask = self.load_robust_matting_alpha_image(sequence, timestep, cam_id, framerate=framerate)

        mask = Image.fromarray(mask)
        mask = mask.resize((image.shape[1], image.shape[0]), resample=Image.BILINEAR)
        mask = np.asarray(mask, dtype="uint8")
        mask = np.expand_dims(mask, axis=2)

        image = image / 255.
        image = image @ color_transform[:3, :3] + color_transform[:3, 3]
        image = np.clip(image, 0, 1)
        mask = mask / 255.
        image = mask * image + (1 - mask) * np.ones_like(image)

        image = image * 255.
        image = np.clip(image, 0, 255)
        image = image.astype(np.uint8)

        return image

        # if self._dataparser_outputs.alpha_channel_filenames is not None:
        #     alpha_channel_filename = self._dataparser_outputs.alpha_channel_filenames[image_idx]
        #     pil_alpha_image = Image.open(alpha_channel_filename)
        #     pil_alpha_image = pil_alpha_image.resize(pil_image.size, resample=Image.BILINEAR)
        #
        #     alpha_image = np.asarray(pil_alpha_image, dtype="uint8")
        #     image = np.concatenate([image, alpha_image[..., None]], axis=-1)

    def load_background_image(self, serial: str) -> np.ndarray:
        return load_img(f"{self.get_sequence_folder('BACKGROUND')}/image_{serial}.png")

    def load_synthetic_background_image(self, cam_id: int) -> np.ndarray:
        return load_img(f"{self.get_sequence_folder('BACKGROUND')}/cam_{cam_id:02d}.png")[:, :, :3]

    def get_timesteps(self, sequence: str, downscale_factor: int = 2, framerate: FrameRateType = '24fps') -> List[int]:
        timestep_folder_regex = re.compile("frame_(\d+)")
        timesteps = []
        for timestep_folder in Path(self.get_sequence_folder(sequence)).iterdir():
            re_match = timestep_folder_regex.match(timestep_folder.name)
            if re_match:
                timestep = int(re_match.group(1))
                if Path(self.get_images_folder(sequence,
                                               timestep,
                                               downscale_factor=downscale_factor,
                                               framerate=framerate)).exists():
                    timesteps.append(timestep)

        timesteps = sorted(timesteps)
        return timesteps

    def list_sequences(self) -> List[str]:
        sequences = []
        if not Path(self.get_sequences_folder()).is_dir():
            return sequences

        for sequence_folder in Path(self.get_sequences_folder()).iterdir():
            if sequence_folder.is_dir() and any(Path(sequence_folder).iterdir()):
                sequences.append(sequence_folder.name)

        return sequences

    def get_n_timesteps_for_sequence(self, sequence_name: str,
                                     downscale_factor: int = 2,
                                     framerate: FrameRateType = '24fps') -> int:
        timesteps = self.get_timesteps(sequence_name, downscale_factor=downscale_factor, framerate=framerate)
        return len(timesteps)

        # sequence_folder = self.get_sequence_folder(sequence_name)
        # if not Path(sequence_folder).is_dir():
        #     return 0
        #
        # # TODO: This is susceptible to failure if there is some other folder in the sequence directory
        # #   Would be better to have an timestep regex check here
        # frame_folders = [child for child in Path(sequence_folder).iterdir() if child.is_dir()]
        #
        # return len(frame_folders)

    def is_calibrated(self) -> bool:
        calibration_folder = Path(self.get_calibration_folder())
        calibration_result_file = Path(self.get_calibration_result_path())
        return calibration_folder.is_dir() and any(calibration_folder.iterdir()) and calibration_result_file.exists()

    def load_calibration_result(self) -> CalibrationResult:
        return CalibrationResult.from_json(load_json(self.get_calibration_result_path()))

    def load_calibration_run_config(self) -> CalibrationRunConfig:
        if self._calibration_run_config is None:
            # Cache calibration_config.json
            # Otherwise, it would be loaded everytime a cam_id -> serial lookup is performed
            self._calibration_run_config = CalibrationRunConfig.from_json(
                load_json(self.get_calibration_run_config_path()))

        return self._calibration_run_config

    # def load_synthetic_stats(self) -> SyntheticReconstructionStats:
    #     return SyntheticReconstructionStats.from_json(load_json(f"{self.get_calibration_folder()}/stats.json"))

    def get_calibration_camera_poses(self) -> List[Pose]:
        """
        Returns
        -------
            Camera extrinsics found via calibration as world_to_cam
        """

        calibration_result = self.load_calibration_result()
        camera_poses = []
        for cam_id in range(calibration_result.params_result.get_n_poses()):
            camera_poses.append(calibration_result.params_result.get_pose(cam_id))

        return camera_poses

    def get_all_calibration_intrinsics(self) -> List[Intrinsics]:
        calibration_result = self.load_calibration_result()
        calibration_config = self.load_calibration_run_config()
        intrinsics = []
        for cam_id in range(calibration_result.params_result.get_n_poses()):
            if calibration_config.optimizer_per_camera_intrinsics:
                intrinsics.append(calibration_result.params_result.get_intrinsics(cam_id))
            else:
                intrinsics.append(calibration_result.params_result.get_intrinsics(0))

        return intrinsics

    def get_calibration_intrinsic_params(self, cam_id: int) -> IntrinsicParams:
        calibration_result = self.load_calibration_result()
        calibration_config = self.load_calibration_run_config()
        cam_id = cam_id if calibration_config.optimizer_per_camera_intrinsics else 0
        return calibration_result.params_result.get_intrinsic_params(cam_id)

    def get_n_cameras(self) -> int:
        return len(self.load_calibration_run_config().serials)

    def load_depth_map(self, sequence_name: str, timestep: int, serial: str, n_cameras: int = 12,
                       framerate: Literal['24fps', '73fps'] = '24fps') -> np.ndarray:
        return np.load(self.get_depth_map_path(sequence_name, timestep, serial, n_cameras, framerate=framerate))[
            'depth_map']

    def load_synthetic_depth_map(self, sequence_name: str, timestep: int, cam_id: int,
                                 n_cameras: int = 16) -> np.ndarray:
        depth_map_path = f"{self.get_depth_maps_folder(sequence_name, timestep, n_cameras)}/cam_{cam_id:02d}.npy"
        return np.load(depth_map_path)

    def load_geometric_depth_map(self, sequence_name: str, timestep: int, serial: str,
                                 n_cameras: int = 16, framerate: Literal['24fps', '73fps'] = '24fps') -> np.ndarray:
        depth_map_path = f"{self.get_geometric_depth_maps_folder(sequence_name, timestep, n_cameras, framerate=framerate)}/cam_{serial}.npz"
        return np.load(depth_map_path)['depth_map']

    def geometric_depth_map_exists(self, sequence_name: str, timestep: int, serial: str,
                                   n_cameras: int = 16, framerate: Literal['24fps', '73fps'] = '24fps') -> bool:
        depth_map_path = f"{self.get_geometric_depth_maps_folder(sequence_name, timestep, n_cameras, framerate=framerate)}/cam_{serial}.npz"
        return Path(depth_map_path).exists()

    def load_normal_map(self, sequence_name: str, timestep: int, serial: str, n_cameras: int = 12,
                        framerate: Literal['24fps', '73fps'] = '24fps') -> np.ndarray:
        return np.load(self.get_normal_map_path(sequence_name, timestep, serial, n_cameras, framerate=framerate))[
            'normal_map']

    def load_geometric_normal_map(self, sequence_name: str, timestep: int, serial: str,
                                  n_cameras: int = 12, framerate: Literal['24fps', '73fps'] = '24fps') -> np.ndarray:
        normal_map_path = f"{self.get_geometric_normal_maps_folder(sequence_name, timestep, n_cameras, framerate=framerate)}/cam_{serial}.npz"
        return np.load(normal_map_path)['normal_map']

    def load_consistency_graph(self,
                               sequence_name: str,
                               timestep: int,
                               serial: Union[str, int],
                               n_cameras: int = 12,
                               framerate: Literal['24fps', '73fps'] = '24fps') -> np.ndarray:
        consistency_graph_path = self.get_consistency_graph_path(sequence_name, timestep, serial, n_cameras=n_cameras,
                                                                 framerate=framerate)
        return np.load(consistency_graph_path)['consistency_graph']

    def load_pointcloud(self,
                        sequence_name: str,
                        timestep: int,
                        n_cameras: int = 12,
                        framerate: Literal['24fps', '73fps'] = '24fps') -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        pcd = o3d.io.read_point_cloud(
            self.get_colmap_pointcloud_path(sequence_name, timestep, n_cameras, framerate=framerate))
        points = np.asarray(pcd.points, dtype=np.float32)
        colors = np.asarray(pcd.colors, dtype=np.float32)
        normals = np.asarray(pcd.normals, dtype=np.float32)
        return points, colors, normals

    def save_color_corrected_image(self,
                                   image: np.ndarray,
                                   sequence_name: str,
                                   serial: str,
                                   timestep: int,
                                   downscale_factor: int = 1,
                                   framerate: FrameRateType = '24fps'):
        image_path = self.get_color_corrected_image_path(sequence_name,
                                                         serial,
                                                         timestep,
                                                         downscale_factor=downscale_factor,
                                                         framerate=framerate)
        save_img(image, image_path)

    def save_mean_image(self, mean_image: np.ndarray, sequence_name: str, cam_id: int, downscale_factor: int = 1):
        serial = self.load_calibration_run_config().serials[cam_id]
        mean_image_path = self.get_mean_image_path(sequence_name, serial, downscale_factor=downscale_factor)
        ensure_directory_exists_for_file(mean_image_path)
        np.savez(mean_image_path, mean_image=mean_image)

    def save_std_image(self, std_image: np.ndarray, sequence_name: str, cam_id: int, downscale_factor: int = 1):
        serial = self.load_calibration_run_config().serials[cam_id]
        std_image_path = self.get_std_image_path(sequence_name, serial, downscale_factor=downscale_factor)
        ensure_directory_exists_for_file(std_image_path)
        np.savez(std_image_path, std_image=std_image)

    def save_median_image(self, median_image: np.ndarray, sequence_name: str, cam_id: int, downscale_factor: int = 1):
        serial = self.load_calibration_run_config().serials[cam_id]
        median_image_path = self.get_median_image_path(sequence_name, serial, downscale_factor=downscale_factor)
        ensure_directory_exists_for_file(median_image_path)
        np.savez(median_image_path, median_image=median_image)

    def load_mean_image(self, sequence_name: str, cam_id: int, dowscale_factor: int = 1) -> np.ndarray:
        serial = self.load_calibration_run_config().serials[cam_id]
        mean_image_path = self.get_mean_image_path(sequence_name, serial, downscale_factor=dowscale_factor)
        return np.load(mean_image_path)["mean_image"]

    def load_std_image(self, sequence_name: str, cam_id: int, dowscale_factor: int = 1) -> np.ndarray:
        serial = self.load_calibration_run_config().serials[cam_id]
        std_image_path = self.get_std_image_path(sequence_name, serial, downscale_factor=dowscale_factor)
        return np.load(std_image_path)["std_image"]

    def load_median_image(self, sequence_name: str, cam_id: int, dowscale_factor: int = 1) -> np.ndarray:
        serial = self.load_calibration_run_config().serials[cam_id]
        median_image_path = self.get_median_image_path(sequence_name, serial, downscale_factor=dowscale_factor)
        return np.load(median_image_path)["median_image"]

    def save_bisenet_segmentation_mask(self, segmentation_mask: np.ndarray, sequence_name: str, timestep: int,
                                       serial: str):
        segmentation_mask_path = self.get_bisenet_segmentation_path(sequence_name, timestep, serial)
        ensure_directory_exists_for_file(segmentation_mask_path)
        np.savez(segmentation_mask_path, segmentation_mask=segmentation_mask)

    def load_bisenet_segmentation_mask(self, sequence_name: str, timestep: int,
                                       serial: str) -> np.ndarray:
        segmentation_mask_path = self.get_bisenet_segmentation_path(sequence_name, timestep, serial)
        return np.load(segmentation_mask_path)["segmentation_mask"]

    def save_bisenet_color_segmentation_mask(self, color_segmentation_mask: np.ndarray, sequence_name: str,
                                             timestep: int, serial: str):
        color_segmentation_mask_path = self.get_bisenet_color_segmentation_path(sequence_name, timestep, serial)
        save_img(color_segmentation_mask, color_segmentation_mask_path)

    def load_bisenet_color_segmentation_mask(self, sequence_name: str, timestep: int, serial: str) -> np.ndarray:
        """
            Label list:
            ===========
            {0: 'background',
                1: 'skin',
                2: 'l_brow',
                3: 'r_brow',
                4: 'l_eye',
                5: 'r_eye',
                6: 'eye_g',
                7: 'l_ear',
                8: 'r_ear',
                9: 'ear_r',
                10: 'nose',
                11: 'mouth',
                12: 'u_lip',
                13: 'l_lip',
                14: 'neck',
                15: 'neck_l',
                16: 'cloth',
                17: 'hair',
                18: 'hat'}
        """

        color_segmentation_mask_path = self.get_bisenet_color_segmentation_path(sequence_name, timestep, serial)
        return load_img(color_segmentation_mask_path)

    def load_facial_landmarks(self, sequence_name: str, timestep: int, serial: str, method: str) -> np.ndarray:
        '''
        method has to be one of ['PIPnet', 'particles']

        Returns np.array of 3D landmarks, where the identity of the k-th landmark is preserved over different timesteps.
        '''
        assert method in ['PIPnet', 'particles']

        facial_landmark_path = self.get_facial_landmarks_path(sequence_name, timestep, serial, method)
        return np.load(facial_landmark_path)

    def load_robust_matting_alpha_image(self,
                                        sequence_name: str,
                                        timestep: int,
                                        cam_id: int,
                                        framerate: FrameRateType,
                                        downscale_factor: int = 1) -> np.ndarray:
        alpha_map_path = self.get_robust_matting_alpha_image_path(sequence_name, timestep, cam_id, framerate=framerate)
        alpha_mask = load_img(alpha_map_path)

        if downscale_factor > 1:
            alpha_mask = Image.fromarray(alpha_mask)
            alpha_mask = alpha_mask.resize((int(alpha_mask.size[0] / downscale_factor),
                                            int(alpha_mask.size[1] / downscale_factor)),
                                           resample=Image.BILINEAR)
            alpha_mask = np.asarray(alpha_mask)

        return alpha_mask

    def load_bboxes(self, sequence_name: str, timestep: int or None, serial: str,
                    framerate: FrameRateType = '24fps') -> np.ndarray:
        '''
        Returns all bounding boxes if timestep is None
        Args:
            sequence_name:
            timestep:
            serial:
            framerate:

        Returns:

        '''

        if self._bboxes[serial] is None:
            bbox_path = self.get_bbox_path(sequence_name, serial)
            if not os.path.exists(bbox_path):
                raise ValueError(
                    'Bounding boxes have note been computed for subject {} in sequence {}.'.format(self._participant_id,
                                                                                                   sequence_name))
            self._bboxes[serial] = np.load(bbox_path)

        if framerate == '24fps':
            if timestep is None:
                return self._bboxes[serial][::3, :]
            else:
                return self._bboxes[serial][3 * timestep]
        else:
            if timestep is None:
                return self._bboxes[serial]
            else:
                return self._bboxes[serial][timestep, :]

    def load_landmarks2D(self, sequence_name: str, timestep: int or None, detector_name: str, serial: str,
                         framerate: FrameRateType = '24fps') -> np.ndarray:
        '''
        Returns all landmakrs when timestep is None.
        Args:
            sequence_name:
            timestep:
            detector_name:
            serial:
            framerate:

        Returns:

        '''
        if self._lms2D[detector_name][serial] is None:
            lms_path = self.get_landmarks2D_path(sequence_name, detector_name, serial)
            if not os.path.exists(lms_path):
                raise ValueError(
                    '{} landmarks have note been computed for subject {} in sequence {}.'.format(detector_name,
                                                                                                 self._participant_id,
                                                                                                 sequence_name))
            self._lms2D[detector_name][serial] = np.load(lms_path)

        if framerate == '24fps':
            if timestep is None:
                return self._lms2D[detector_name][serial][::3, :, :]
            else:
                return self._lms2D[detector_name][serial][3 * timestep, ...]
        else:
            if timestep is None:
                return self._lms2D[detector_name][serial]
            else:
                return self._lms2D[detector_name][serial][timestep, ...]

    def load_landmarks3D(self, sequence_name: str, timestep: int or None, detector_name: str, serial: str,
                         framerate: FrameRateType = '24fps') -> np.ndarray:
        '''
        Returns all landmakrs when timestep is None.
        Args:
            sequence_name:
            timestep:
            detector_name:
            serial:
            framerate:

        Returns:

        '''
        if self._lms3D[detector_name][serial] is None:
            lms_path = self.get_landmarks3D_path(sequence_name, detector_name, serial)
            if not os.path.exists(lms_path):
                print('Desired path ' + lms_path + ' does not exit!')
                raise ValueError(
                    '{} landmarks have note been computed for subject {} in sequence {}.'.format(detector_name,
                                                                                                 self._participant_id,
                                                                                                 sequence_name))
            self._lms3D[detector_name][serial] = np.load(lms_path)

        if framerate == '24fps':
            if timestep is None:
                return self._lms3D[detector_name][serial][::3, :, :]
            else:
                return self._lms3D[detector_name][serial][3 * timestep, ...]
        else:
            if timestep is None:
                return self._lms3D[detector_name][serial]
            else:
                return self._lms3D[detector_name][serial][timestep, ...]

    def load_3DMM_tracking(self, sequence: str, mm_name: str):
        tracking_folder = self.get_3DMM_tracking_folder(sequence, mm_name)
        return np.load(f"{tracking_folder}/tracked_flame_params.npz")

    def load_affine_color_correction(self, sequence_name: str, serial: str):
        if self._color_corrections[serial] is None:
            color_correction_path = self.get_color_correction_path(sequence_name, serial)
            self._color_corrections[serial] = np.load(color_correction_path)

        return self._color_corrections[serial]

    def load_psr_reconstructions(self, sequence_name: str, timestep: int,
                                 framerate: FrameRateType = '24fps') -> trimesh.Trimesh:
        psr_pth = self.get_psr_reconstruction_path(sequence_name, timestep, framerate)
        return trimesh.load(psr_pth)

    def save_bboxes(self, bboxes: np.ndarray, sequence_name: str, serial: str):
        bbox_path = self.get_bbox_path(sequence_name, serial)
        ensure_directory_exists_for_file(bbox_path)
        np.save(bbox_path, bboxes)

    def save_landmarks2D(self, lms: np.ndarray, sequence_name: str, detector_name: str, serial: str):
        lms_path = self.get_landmarks2D_path(sequence_name, detector_name, serial)
        ensure_directory_exists_for_file(lms_path)
        np.save(lms_path, lms)

    def save_landmarks3D(self, lms: np.ndarray, sequence_name: str, detector_name: str, serial: str):
        lms_path = self.get_landmarks3D_path(sequence_name, detector_name, serial)
        ensure_directory_exists_for_file(lms_path)
        np.save(lms_path, lms)

    def save_heatmaps(self, heatmaps: np.ndarray, sequence_name: str, detector_name: str, serial: str):
        heatmaps_path = self.get_heatmaps_path(sequence_name, detector_name, serial)
        ensure_directory_exists_for_file(heatmaps_path)
        np.savez(heatmaps_path, heatmaps=heatmaps)

    def save_affine_color_correction(self, color_transform: np.ndarray, sequence_name: str, serial: str):
        color_correction_path = self.get_color_correction_path(sequence_name, serial)
        ensure_directory_exists_for_file(color_correction_path)
        np.save(color_correction_path, color_transform)

    # ----------------------------------------------------------
    # Folders
    # ----------------------------------------------------------

    def get_image_file_name_format(self,
                                   has_downsample_factor: bool = False,
                                   is_foreground_only: bool = False,
                                   has_framerate: bool = False) -> str:
        if is_foreground_only:
            image_folder_name = 'foreground'
        else:
            image_folder_name = 'images'

        if has_downsample_factor:
            image_folder_name = image_folder_name + "-{f:}x"

        if has_framerate:
            image_folder_name = image_folder_name + "-{r:}"

        return "{s:}/frame_{t:05d}/" + image_folder_name + "/cam_{c:}.png"

    def get_sequences_folder(self, relative: bool = False) -> str:
        if relative:
            return "sequences"
        else:
            return f"{self._location}/sequences"

    def get_calibration_folder(self) -> str:
        return f"{self._location}/calibration"

    def get_visualizations_folder(self) -> str:
        return f"{self._location}/visualizations"

    def get_annotations_folder(self, relative: bool = False) -> str:
        if relative:
            return "annotations"
        else:
            return f"{self._location}/annotations"

    def get_sequence_folder(self, sequence: str, relative: bool = False) -> str:
        return f"{self.get_sequences_folder(relative=relative)}/{sequence}"

    def get_timestep_folder(self, sequence: str, timestep: int, relative: bool = False) -> str:
        return f"{self.get_sequence_folder(sequence, relative=relative)}/frame_{timestep:05d}"

    def get_bbox_folder(self, sequence: str, relative: bool = False) -> str:
        return f"{self.get_annotations_folder(relative=relative)}/bbox/{sequence}"

    def get_landmarks2D_folder(self, sequence: str, detector_name: str, relative: bool = False) -> str:
        assert detector_name in self.valid_landmark_detectors
        return f"{self.get_annotations_folder(relative=relative)}/landmarks2D/{sequence}/{detector_name}"

    def get_heatmaps_folder(self, sequence: str, detector_name: str, relative: bool = False) -> str:
        assert detector_name in self.valid_landmark_detectors
        return f"{self.get_annotations_folder(relative=relative)}/heatmaps/{sequence}/{detector_name}"

    def get_landmarks3D_folder(self, sequence: str, detector_name: str, relative: bool = False) -> str:
        assert detector_name in self.valid_landmark_detectors
        return f"{self.get_annotations_folder(relative=relative)}/landmarks3D/{sequence}/{detector_name}"

    def get_3DMM_tracking_folder(self, sequence: str, mm_name: str, relative: bool = False) -> str:
        return f"{self.get_annotations_folder(relative=relative)}/tracking/{sequence}/{mm_name}"

    def get_color_correction_folder(self, sequence_name: str, relative: bool = False) -> str:
        return f"{self.get_annotations_folder(relative=relative)}/{sequence_name}/color_correction/"

    def get_images_folder(self,
                          sequence: str,
                          timestep: int,
                          downscale_factor: int = 1,
                          framerate: FrameRateType = '24fps',
                          relative: bool = False) -> str:
        image_folder_name = self.get_image_folder_name(downscale_factor=downscale_factor, framerate=framerate)
        return f"{self.get_timestep_folder(sequence, timestep, relative=relative)}/{image_folder_name}"

    def get_image_folder_name(self,
                              downscale_factor: int = 1,
                              framerate: FrameRateType = '24fps') -> str:
        folder_name = "images" if downscale_factor == 1 else f"images-{downscale_factor}x"
        if framerate == '73fps':
            folder_name = f"{folder_name}-73fps"

        return folder_name

    def get_robust_matting_alpha_folder(self,
                                        sequence: str,
                                        timestep: int,
                                        framerate: FrameRateType = '24fps',
                                        relative: bool = False) -> str:
        alpha_map_folder_name = "alpha_map"
        if framerate == '73fps':
            alpha_map_folder_name = f"{alpha_map_folder_name}-73fps"
        return f"{self.get_timestep_folder(sequence, timestep, relative=relative)}/{alpha_map_folder_name}"

    def get_colmap_folder(self, sequence: str, timestep: int, relative: bool = False,
                          framerate: FrameRateType = '24fps') -> str:
        colmap_folder_name = "colmap"
        if framerate != '24fps':
            colmap_folder_name += f"-{framerate}"

        return f"{self.get_timestep_folder(sequence, timestep, relative=relative)}/{colmap_folder_name}"

    def get_pointclouds_visualizations_folder(self, sequence_name: str) -> str:
        return f"{self.get_visualizations_folder()}/pointclouds/{sequence_name}"

    def get_depth_maps_folder(self, sequence_name: str, timestep: int, n_cameras: int,
                              framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_colmap_folder(sequence_name, timestep, framerate=framerate)}/depth_maps/{n_cameras}"

    def get_normal_maps_folder(self, sequence_name: str, timestep: int, n_cameras: int = 12,
                               framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_colmap_folder(sequence_name, timestep, framerate=framerate)}/normal_maps/{n_cameras}"

    def get_geometric_depth_maps_folder(self, sequence_name: str, timestep: int, n_cameras: int,
                                        framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_colmap_folder(sequence_name, timestep, framerate=framerate)}/depth_maps_geometric/{n_cameras}"

    def get_geometric_normal_maps_folder(self, sequence_name: str, timestep: int, n_cameras: int,
                                         framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_colmap_folder(sequence_name, timestep, framerate=framerate)}/normal_maps_geometric/{n_cameras}"

    def get_consistency_graphs_folder(self, sequence_name: str, timestep: int, n_cameras: int,
                                      framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_colmap_folder(sequence_name, timestep, framerate=framerate)}/consistency_graphs/{n_cameras}"

    def get_bisenet_segmentations_folder(self, sequence_name: str, timestep: int) -> str:
        return f"{self.get_timestep_folder(sequence_name, timestep)}/bisenet_segmentation_masks"

    def get_facial_landmarks_folder(self, sequence_name: str, timestep: int, method: str) -> str:
        if method == 'PIPnet':
            return f"{self.get_timestep_folder(sequence_name, timestep)}/lms3D"
        elif method == 'particles':
            return f"{self.get_timestep_folder(sequence_name, timestep)}/particles3D"

    def get_landmark_annotation_folder(self, sequence_name: str, detector_name: str, serial: str) -> str:
        assert detector_name in self.valid_landmark_detectors
        return f"{self.get_annotations_folder()}/annotated_images/{sequence_name}/{detector_name}/cam_{serial}"

    def get_color_corrected_images_folder(self,
                                          sequence_name: str,
                                          timestep: int,
                                          downscale_factor: int = 1,
                                          framerate: FrameRateType = '24fps'):
        return f"{self.get_timestep_folder(sequence_name, timestep)}/color_corrected_{downscale_factor}x-{framerate}"

    def get_psr_reconstruction_folder(self, sequence_name: str) -> str:
        return f"{self._location}/../../PSR/{self._participant_id:03d}/{sequence_name}/12/pointclouds"

    # ----------------------------------------------------------
    # Paths
    # ----------------------------------------------------------

    def get_relative_image_path(self,
                                sequence: str,
                                serial: str,
                                timestep: int,
                                downsample_factor: int = 1,
                                framerate: FrameRateType = '24pfs',
                                foreground_only: bool = False) -> str:

        has_downsample_factor = downsample_factor > 1
        has_framerate = framerate != '24fps'

        image_file_name_format = self.get_image_file_name_format(has_downsample_factor=has_downsample_factor,
                                                                 is_foreground_only=foreground_only,
                                                                 has_framerate=has_framerate)

        format_args = {
            's': sequence,
            't': timestep,
            'c': serial
        }

        if has_downsample_factor:
            format_args['f'] = downsample_factor

        if has_framerate:
            format_args['r'] = framerate

        image_file_name = image_file_name_format.format(**format_args)

        # if downsample_factor > 1:
        #     image_file_name = image_file_name_format.format(s=sequence, t=timestep, c=serial, f=downsample_factor)
        # else:
        #     image_file_name = image_file_name_format.format(s=sequence, t=timestep, c=serial)
        return image_file_name

    def get_image_path(self,
                       sequence: str,
                       serial: str,
                       timestep: int,
                       downsample_factor: int = 1,
                       framerate: FrameRateType = '24fps',
                       foreground_only: bool = False) -> str:
        relative_image_path = self.get_relative_image_path(
            sequence,
            serial,
            timestep,
            downsample_factor=downsample_factor,
            framerate=framerate,
            foreground_only=foreground_only
        )
        return f"{self.get_sequences_folder()}/{relative_image_path}"

    def get_image_path_for_cam_id(self,
                                  sequence: str,
                                  cam_id: int,
                                  timestep: int,
                                  downsample_factor: int = 1,
                                  framerate: FrameRateType = '24fps',
                                  foreground_only: bool = False) -> str:
        calibration_config = self.load_calibration_run_config()
        serial = calibration_config.serials[cam_id]

        return self.get_image_path(sequence,
                                   serial,
                                   timestep,
                                   downsample_factor=downsample_factor,
                                   framerate=framerate,
                                   foreground_only=foreground_only)

    def get_robust_matting_alpha_image_path(self,
                                            sequence: str,
                                            timestep: int,
                                            cam_id: int,
                                            framerate: FrameRateType = '24fps') -> str:
        calibration_config = self.load_calibration_run_config()
        serial = calibration_config.serials[cam_id]
        return f"{self.get_robust_matting_alpha_folder(sequence, timestep, framerate=framerate)}/cam_{serial}.png"

    def get_synthetic_image_path_for_cam_id(self, sequence: str, cam_id: int, timestep: int) -> str:
        images_folder = self.get_images_folder(sequence, timestep)
        return f"{images_folder}/cam_{cam_id:02d}.png"

    # TODO: Pointcloud with camera IDs, e.g., pointcloud_7.ply
    def get_colmap_pointcloud_path(self,
                                   sequence: str,
                                   timestep: int,
                                   n_cameras: int = 12,
                                   ignore_not_exist: bool = False,
                                   framerate: Literal['24fps', '73fps'] = '24fps') -> str:
        pointcloud_path = f"{self.get_colmap_folder(sequence, timestep, framerate=framerate)}/pointclouds/pointcloud_{n_cameras}.ply"
        if not ignore_not_exist and not Path(pointcloud_path).exists():
            # Using old deprecated pointcloud path
            pointcloud_path = f"{self.get_colmap_folder(sequence, timestep, framerate=framerate)}/pointcloud_{n_cameras}.ply"
            if Path(pointcloud_path).exists():
                print(
                    "Using deprecated pointcloud path. Consider moving the pointclouds into the colmap/pointclouds directory")

        if not ignore_not_exist:
            assert Path(pointcloud_path).exists(), f"No pointcloud found at {pointcloud_path}. Maybe COLMAP didn't " \
                                                   f"run yet? (Run scripts/colmap/create_pointcloud.ply)"

        return pointcloud_path

    def get_calibration_result_path(self) -> str:
        return f"{self.get_calibration_folder()}/calibration_result.json"

    def get_calibration_run_config_path(self) -> str:
        return f"{self.get_calibration_folder()}/config.json"

    def get_single_timestep_transforms_path(self,
                                            sequence_name: str,
                                            timestep: int,
                                            downscale_factor: int = 1,
                                            framerate: FrameRateType = '24fps',
                                            use_color_correction: bool = False):
        timestep_folder = self.get_timestep_folder(sequence_name, timestep)
        transforms_name = 'transforms'

        if downscale_factor != 1:
            transforms_name = f"{transforms_name}_{downscale_factor}x"

        if framerate != '24fps':
            transforms_name = f"{transforms_name}-{framerate}"

        if use_color_correction:
            transforms_name = f"{transforms_name}_color-corrected"

        transforms_path = f"{timestep_folder}/{transforms_name}.json"

        return transforms_path

    def get_depth_map_path(self,
                           sequence_name: str,
                           timestep: int,
                           serial: str,
                           n_cameras: int = 12,
                           framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_depth_maps_folder(sequence_name, timestep, n_cameras, framerate=framerate)}/cam_{serial}.npz"

    def get_normal_map_path(self,
                            sequence_name: str,
                            timestep: int,
                            serial: str,
                            n_cameras: int = 12,
                            framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_normal_maps_folder(sequence_name, timestep, n_cameras, framerate=framerate)}/cam_{serial}.npz"

    def get_consistency_graph_path(self,
                                   sequence_name: str,
                                   timestep: int,
                                   serial: str,
                                   n_cameras: int = 12,
                                   framerate: FrameRateType = '24fps') -> str:
        return f"{self.get_consistency_graphs_folder(sequence_name, timestep, n_cameras, framerate=framerate)}/cam_{serial}.npz"

    def get_mean_image_path(self, sequence_name: str, serial: str, downscale_factor: int = 1) -> str:
        return f"{self._location}/statistics/mean_images/{sequence_name}/{downscale_factor}x/cam_{serial}.npz"

    def get_std_image_path(self, sequence_name: str, serial: str, downscale_factor: int = 1) -> str:
        return f"{self._location}/statistics/std_images/{sequence_name}/{downscale_factor}x/cam_{serial}.npz"

    def get_median_image_path(self, sequence_name: str, serial: str, downscale_factor: int = 1) -> str:
        return f"{self._location}/statistics/median_images/{sequence_name}/{downscale_factor}x/cam_{serial}.npz"

    def get_bisenet_segmentation_path(self, sequence_name: str, timestep: int, serial: str) -> str:
        return f"{self.get_bisenet_segmentations_folder(sequence_name, timestep)}/segmentation_cam_{serial}.npz"

    def get_bisenet_color_segmentation_path(self, sequence_name: str, timestep: int, serial: str) -> str:
        return f"{self.get_bisenet_segmentations_folder(sequence_name, timestep)}/color_segmentation_cam_{serial}.png"

    def get_bbox_path(self, sequence_name: str, serial: str) -> str:
        return f"{self.get_bbox_folder(sequence_name)}/{serial}.npy"

    def get_landmarks2D_path(self, sequence_name: str, detector_name: str, serial: str) -> str:
        return f"{self.get_landmarks2D_folder(sequence_name, detector_name)}/{serial}.npy"

    def get_heatmaps_path(self, sequence_name: str, detector_name: str, serial: str) -> str:
        return f"{self.get_heatmaps_folder(sequence_name, detector_name)}/{serial}.npy"

    def get_landmarks3D_path(self, sequence_name: str, detector_name: str, serial: str) -> str:
        return f"{self.get_landmarks3D_folder(sequence_name, detector_name)}/{serial}.npy"
        # return f"{self.get_annotations_folder(relative=False)}/smoothed_landmarks3D/{sequence_name}_{detector_name}.npy"

    def get_facial_landmarks_path(self, sequence_name: str, timestep: int, serial: str, method: str) -> str:
        return f"{self.get_facial_landmarks_folder(sequence_name, timestep, method)}/cam_{serial}.npy"

    def get_landmark_annotation_path(self, sequence_name: str, timestep: int, detector_name: str, serial: str, ) -> str:
        return f"{self.get_landmark_annotation_folder(sequence_name, detector_name, serial)}/{timestep:05d}.jpg"

    def get_color_correction_path(self, sequence_name: str, serial: str) -> str:
        return f"{self.get_color_correction_folder(sequence_name)}/{serial}.npy"

    def get_psr_reconstruction_path(self, sequence_name: str, timestep: int, framerate: FrameRateType = '24fps'):
        frame = timestep
        if framerate == '24fps':
            frame *= 3
        return f"{self.get_psr_reconstruction_folder(sequence_name)}/frame_{frame:05d}.ply"

    def get_color_corrected_image_path(self,
                                       sequence_name: str,
                                       serial: str,
                                       timestep: int,
                                       downscale_factor: int = 1,
                                       framerate: FrameRateType = '24fps'):
        folder = self.get_color_corrected_images_folder(sequence_name,
                                                        timestep,
                                                        downscale_factor=downscale_factor,
                                                        framerate=framerate)
        return f"{folder}/cam_{serial}.png"

    def __iter__(self) -> Iterator:
        raise NotImplementedError()

    def _save(self, data: Any):
        raise NotImplementedError()


class ProcessedCaptureDataFolder(DataFolder[ProcessedCaptureDataManager]):

    def __init__(self):
        super(ProcessedCaptureDataFolder, self).__init__(FAMUDY_PROCESSED_CAPTURE_DATA_PATH, localize_via_run_name=True)

    def list_participants(self) -> List[int]:
        participants = []
        participant_regex = re.compile("0*(\d+)")
        for folder in Path(self._location).iterdir():
            match = participant_regex.match(folder.name)
            if match:
                participants.append(int(match.group(1)))
        participants = sorted(participants)

        return participants
