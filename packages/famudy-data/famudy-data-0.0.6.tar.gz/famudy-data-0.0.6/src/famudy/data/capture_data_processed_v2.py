import csv
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Union, Tuple

import numpy as np
import openctm
import pandas as pd
import trimesh
from PIL import Image
from elias.util import ensure_directory_exists, load_json, load_img, save_img
import open3d as o3d

from famudy.config.bbox import BoundingBox
from famudy.config.run.calibration import CalibrationResult, CalibrationRunConfig
from famudy.config.run.calibration_params import IntrinsicParams
from famudy.env_data import FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW, FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW
from famudy.util.quantization import DepthQuantizer, NormalsQuantizer, CanonicalCoordinatesQuantizer

DEFAULT_DF: int = 2  # Default downscale_factor
CAM_ID_SERIAL_TYPE = Union[str, int]
WFLW_2_iBUG68 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 33, 34, 35, 36, 37, 42, 43, 44, 45, 46,
                 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 67, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 80,
                 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]


@dataclass
class ImageMetadata:
    participant_id: int
    sequence_name: str
    timestep: int
    serial: str


class FamudyParticipantDataManager:
    def __init__(self, participant_id: int, remote: bool = False):
        capture_data_path = FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW if remote else FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW
        self._location = f"{capture_data_path}/{participant_id:03d}"

        self._participant_id = participant_id
        self._remote = remote
        self._closest_calibrated_participant_id = None
        self._calibration_run_config = None

    # ----------------------------------------------------------
    # General
    # ----------------------------------------------------------

    def get_participant_id(self) -> int:
        return self._participant_id

    # ----------------------------------------------------------
    # Calibration
    # ----------------------------------------------------------

    def load_calibration_result(self) -> CalibrationResult:
        if not self.has_calibration_result():
            if self._closest_calibrated_participant_id is None:
                self._closest_calibrated_participant_id = self.find_closest_calibrated_participant_id()

            closest_data_manager = FamudyParticipantDataManager(self._closest_calibrated_participant_id,
                                                                remote=self._remote)
            return CalibrationResult.from_json(load_json(closest_data_manager.get_calibration_result_path()))
        else:
            return CalibrationResult.from_json(load_json(self.get_calibration_result_path()))

    def has_calibration_result(self) -> bool:
        return Path(self.get_calibration_result_path()).exists()

    def load_calibration_run_config(self) -> CalibrationRunConfig:
        if self._calibration_run_config is None:
            # Cache calibration_config.json
            # Otherwise, it would be loaded everytime a cam_id -> serial lookup is performed

            if not self.has_calibration_result():
                if self._closest_calibrated_participant_id is None:
                    self._closest_calibrated_participant_id = self.find_closest_calibrated_participant_id()

                closest_data_manager = FamudyParticipantDataManager(self._closest_calibrated_participant_id,
                                                                    remote=self._remote)
                calibration_run_config = CalibrationRunConfig.from_json(
                    load_json(closest_data_manager.get_calibration_run_config_path()))
            else:
                calibration_run_config = CalibrationRunConfig.from_json(
                    load_json(self.get_calibration_run_config_path()))

            self._calibration_run_config = calibration_run_config

        return self._calibration_run_config

    def get_calibration_intrinsic_params(self, cam_id: int) -> IntrinsicParams:
        calibration_result = self.load_calibration_result()
        calibration_config = self.load_calibration_run_config()
        cam_id = cam_id if calibration_config.optimizer_per_camera_intrinsics else 0
        return calibration_result.params_result.get_intrinsic_params(cam_id)

    def get_calibration_folder(self) -> str:
        return f"{self._location}/calibration"

    def get_calibration_result_path(self) -> str:
        return f"{self.get_calibration_folder()}/calibration_result.json"

    def get_calibration_run_config_path(self) -> str:
        return f"{self.get_calibration_folder()}/config.json"

    # ----------------------------------------------------------
    # Find closest calibration participant
    # ----------------------------------------------------------

    def find_closest_calibrated_participant_id(self) -> int:
        data_folder = FamudyParticipantDataFolder(remote=self._remote)

        calibrated_participant_ids = set(data_folder.list_calibrated_participants())
        data_location = data_folder.get_location()
        # meta_data_path = f"{data_location}/participants_meta_data_05_23_23.csv"
        meta_data_path = f"{data_location}/participants_meta_data.csv"

        with open(meta_data_path) as f:
            csv_reader = csv.reader(f, delimiter=',')
            column_names = next(csv_reader)
            rows = []
            for row in csv_reader:
                rows.append(row)

        columns = list(zip(*rows))
        idx_timestamp = column_names.index("Timestamp")
        idx_participant_id = column_names.index("ID")

        timestamps = columns[idx_timestamp]
        timestamps = [datetime.strptime(timestamp, "%d/%m/%Y %H:%M:%S") for timestamp in timestamps]

        participant_ids = columns[idx_participant_id]
        participant_ids = [-1 if p_id == 'x' else int(p_id) for p_id in participant_ids]

        calibrated = [p_id in calibrated_participant_ids for p_id in participant_ids]

        calibrated_timestamps = [timestamp for timestamp, is_calibrated in zip(timestamps, calibrated) if is_calibrated]
        calibrated_p_ids = [p_id for p_id, is_calibrated in zip(participant_ids, calibrated) if is_calibrated]

        if self._participant_id not in participant_ids:
            raise ValueError(f"Could not find {self._participant_id} in {meta_data_path}. Maybe it is not up-to-date?")
        i_row_reference_session = participant_ids.index(self._participant_id)
        reference_timestamp = timestamps[i_row_reference_session]

        time_differences_to_calibrated = [abs(timestamp - reference_timestamp) for timestamp in calibrated_timestamps]
        idx_closest = np.argmin(time_differences_to_calibrated)
        closest_calibrated_participant_id = calibrated_p_ids[idx_closest]

        print(
            f"Using calibration of {closest_calibrated_participant_id} instead of requested {self._participant_id} ({min(time_differences_to_calibrated)} apart)")

        return closest_calibrated_participant_id

    # ----------------------------------------------------------
    # Sequences
    # ----------------------------------------------------------

    # /sequences
    def get_sequences_folder(self) -> str:
        return f"{self._location}/sequences"

    # /sequences/$SEQUENCE_NAME
    def get_sequence_folder(self, sequence_name: str) -> str:
        return f"{self.get_sequences_folder()}/{sequence_name}"

    def list_sequences(self, include_calibration: bool = False, include_background: bool = False) -> List[str]:
        sequences = []
        for sequence_folder in Path(self.get_sequences_folder()).iterdir():
            sequence = sequence_folder.name
            if sequence == 'BACKGROUND':
                if include_background:
                    sequences.append(sequence)
            elif sequence in {'CALIB', 'CALIB_COLOR'}:
                if include_calibration:
                    sequences.append(sequence)
            else:
                sequences.append(sequence)

        sequences = sorted(sequences)

        return sequences

    def has_sequence(self, sequence_name: str) -> bool:
        return Path(self.get_sequence_folder(sequence_name)).exists()


class FamudySequenceDataManager:

    def __init__(self,
                 participant_id: int,
                 sequence_name: str,
                 create_if_not_exists: bool = False,
                 remote: bool = False,
                 relative: bool = False,
                 downscale_factor: int = DEFAULT_DF):
        processed_capture_data_path = FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW if remote else FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW
        if create_if_not_exists:
            ensure_directory_exists(f"{processed_capture_data_path}/{participant_id:03d}")

        self._location = f"{processed_capture_data_path}/{participant_id:03d}"

        self._participant_id = participant_id
        self._sequence_name = sequence_name

        self._relative = relative
        self._downscale_factor = downscale_factor

        self._participant_data_manager = FamudyParticipantDataManager(participant_id, remote=remote)

        self._serials = None

        self._depth_quantizer = DepthQuantizer()
        self._normals_quantizer = NormalsQuantizer()

    # ==========================================================
    # General
    # ==========================================================

    @property
    def serials(self) -> List[str]:
        if self._serials is None:
            self._serials = self._participant_data_manager.load_calibration_run_config().serials

        return self._serials

    def get_participant_id(self) -> int:
        return self._participant_id

    def get_sequence_name(self) -> str:
        return self._sequence_name

    def get_timesteps(self) -> List[int]:
        timestep_folder_regex = re.compile("frame_(\d+)")
        timesteps = []
        for timestep_folder in Path(self.get_timesteps_folder()).iterdir():
            re_match = timestep_folder_regex.match(timestep_folder.name)
            if re_match:
                timestep = int(re_match.group(1))
                if Path(self.get_images_folder(timestep)).exists():
                    timesteps.append(timestep)

        timesteps = sorted(timesteps)
        return timesteps

    def get_n_timesteps(self) -> int:
        return len(self.get_timesteps())

    # ==========================================================
    # Assets
    # ==========================================================
    # Calibration
    # ----------------------------------------------------------

    def load_calibration_result(self) -> CalibrationResult:
        return self._participant_data_manager.load_calibration_result()

    def has_calibration_result(self) -> bool:
        return self._participant_data_manager.has_calibration_result()

    def load_calibration_run_config(self) -> CalibrationRunConfig:
        return self._participant_data_manager.load_calibration_run_config()

    def get_calibration_intrinsic_params(self, cam_id: int) -> IntrinsicParams:
        return self._participant_data_manager.get_calibration_intrinsic_params(cam_id)

    # ----------------------------------------------------------
    # Images
    # ----------------------------------------------------------

    def cam_id_to_serial(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        if isinstance(cam_id_or_serial, int):
            return self.serials[cam_id_or_serial]
        else:
            return cam_id_or_serial

    def serial_to_cam_id(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> int:
        if isinstance(cam_id_or_serial, str):
            return self.serials.index(cam_id_or_serial)
        else:
            return cam_id_or_serial

    def load_image(self,
                   timestep: int,
                   cam_id_or_serial: CAM_ID_SERIAL_TYPE,
                   use_color_correction: bool = False,
                   use_robust_matting_mask: bool = False) -> np.ndarray:

        image_path = self.get_image_path(timestep, cam_id_or_serial)
        # TODO: workaround only necessary as long not all EXP-1-head sequences have been processed again
        if not Path(image_path).exists():
            image_path = image_path[:-3] + 'png'
        image = load_img(image_path)

        if use_color_correction:
            image = image / 255.  # Cast to float
            affine_color_transform = np.load(self.get_color_correction_path(cam_id_or_serial))
            image = image @ affine_color_transform[:3, :3] + affine_color_transform[np.newaxis, :3, 3]
            image = np.clip(image, 0, 1)
            image = (image * 255).astype(np.uint8)

        if use_robust_matting_mask:
            mask = self.load_robust_matting_alpha_image(timestep, cam_id_or_serial)

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

    def has_image(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> bool:
        image_path = self.get_image_path(timestep, cam_id_or_serial)
        return Path(image_path).exists()

    def load_robust_matting_alpha_image(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> np.ndarray:
        alpha_map_path = self.get_robust_matting_alpha_image_path(timestep, cam_id_or_serial)
        alpha_mask = load_img(alpha_map_path)

        if self._downscale_factor > 1:
            alpha_mask = Image.fromarray(alpha_mask)
            alpha_mask = alpha_mask.resize((int(alpha_mask.size[0] / self._downscale_factor),
                                            int(alpha_mask.size[1] / self._downscale_factor)),
                                           resample=Image.BILINEAR)
            alpha_mask = np.asarray(alpha_mask)

        return alpha_mask

    # ----------------------------------------------------------
    # COLMAP
    # ----------------------------------------------------------

    def depth_map_exists(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE, n_cameras: int = 12) -> bool:
        return Path(self.get_depth_map_path(timestep, cam_id_or_serial, n_cameras)).exists()

    def load_depth_map(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE, n_cameras: int = 12) -> np.ndarray:
        depth_map_path = self.get_depth_map_path(timestep, cam_id_or_serial, n_cameras)
        return self._depth_quantizer.decode(load_img(depth_map_path))
        # return np.load(depth_map_path)['depth_map']

    def load_normal_map(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE, n_cameras: int = 12) -> np.ndarray:
        normal_map_path = self.get_normal_map_path(timestep, cam_id_or_serial, n_cameras)
        return self._normals_quantizer.decode(load_img(normal_map_path))
        # return np.load(normal_map_path)['normal_map']

    def load_consistency_graph(self,
                               timestep: int,
                               cam_id_or_serial: CAM_ID_SERIAL_TYPE,
                               n_cameras: int = 12) -> np.ndarray:
        consistency_graph_path = self.get_consistency_graph_path(timestep, cam_id_or_serial, n_cameras=n_cameras)
        return np.load(consistency_graph_path)['consistency_graph']

    def load_point_cloud(self, timestep: int, n_cameras: int = 12) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        pointcloud_path = self.get_point_cloud_path(timestep, n_cameras=n_cameras)
        pcd = o3d.io.read_point_cloud(pointcloud_path)

        points = np.asarray(pcd.points, dtype=np.float32)
        colors = np.asarray(pcd.colors, dtype=np.float32)
        normals = np.asarray(pcd.normals, dtype=np.float32)
        return points, colors, normals

    # ----------------------------------------------------------
    # Segmentation Mask
    # ----------------------------------------------------------

    def load_bisenet_segmentation_mask(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> np.ndarray:
        """
            Label list:
            ===========
            {
                0: 'background',
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
                18: 'hat'
            }
        """
        segmentation_mask_path = self.get_bisenet_segmentation_path(timestep, cam_id_or_serial)
        return load_img(segmentation_mask_path)

    def has_facer_segmentation_masks(self, timestep: int) -> bool:
        segmentations_folder = self.get_facer_segmentations_folder(timestep)
        return Path(segmentations_folder).exists() and len(list(Path(segmentations_folder).iterdir())) > 0

    def load_facer_segmentation_mask(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> np.ndarray:
        """
                    Label list:
                    ===========
                    {
                        0: 'background',
                        1: 'neck',
                        2: 'face',
                        3: 'torso',
                        4: 'r_ear?',
                        5: 'l_ear',
                        6: 'r_brow',
                        7: 'l_brow',
                        8: 'r_eye',
                        9: 'l_eye',
                        10: 'nose',
                        11: 'mouth?',
                        12: 'l_lip',
                        13: 'u_lip',
                        14: 'hair',

                    }
                """
        segmentation_mask_path = self.get_facer_segmentation_path(timestep, cam_id_or_serial)
        return load_img(segmentation_mask_path)

    def save_facer_segmentation_mask(self,
                                     segmentation_mask: np.ndarray,
                                     timestep: int,
                                     cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> np.ndarray:
        segmentation_mask_path = self.get_facer_segmentation_path(timestep, cam_id_or_serial)
        save_img(segmentation_mask, segmentation_mask_path)

    # ----------------------------------------------------------
    # Landmarks + Bounding Box
    # ----------------------------------------------------------

    def has_2d_landmarks(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> bool:
        return Path(self.get_2d_landmarks_path(cam_id_or_serial)).exists()

    def load_2d_landmarks(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE, use_ibug_68: bool = False) -> np.ndarray:
        landmarks_2d = np.load(self.get_2d_landmarks_path(cam_id_or_serial))

        if use_ibug_68:
            landmarks_2d = landmarks_2d[:, WFLW_2_iBUG68]

        return landmarks_2d

    def has_3d_landmarks(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> bool:
        return Path(self.get_3d_landmarks_path(cam_id_or_serial)).exists()

    def load_3d_landmarks(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> np.ndarray:
        landmarks_3d = np.load(self.get_3d_landmarks_path(cam_id_or_serial))
        return landmarks_3d

    def load_bounding_boxes(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> List[BoundingBox]:
        """
        Bounding boxes are [T, 5] that contains for each timestep:
         - x, y
         - width, height
         - confidence
        of the detected face bounding box
        """

        bounding_boxes = np.load(self.get_bounding_boxes_path(cam_id_or_serial))
        bounding_boxes = [BoundingBox(x=bbox[0], y=bbox[1], width=bbox[2], height=bbox[3], score=bbox[4])
                          for bbox in bounding_boxes]
        return bounding_boxes

    # ----------------------------------------------------------
    # Tracking
    # ----------------------------------------------------------

    def load_3DMM_tracking(self, mm_name: str) -> np.ndarray:
        tracking_folder = self.get_3DMM_tracking_folder(mm_name)
        return np.load(f"{tracking_folder}/tracked_flame_params.npz")
        # return np.load(f"{tracking_folder}/params.npz")

    def load_corrective_transform(self, mm_name: str) -> np.ndarray:
        """
        4 x FLAME_2_NPHM x MVS_2_FLAME
        """
        tracking_folder = self.get_3DMM_tracking_folder(mm_name)
        return np.load(f"{tracking_folder}/corrective_transform.npz")

    def load_NPHM_mesh(self, timestep: int,
                       mm_name: str = 'NPHM',
                       include_canonical_coordinates: bool = False) -> trimesh.Trimesh:
        mesh_path = self.get_NPHM_mesh_path(timestep, mm_name=mm_name)
        mesh = openctm.import_mesh(mesh_path)

        if include_canonical_coordinates:
            # Canonical coordinates need to be decoded from uint16 quantization
            canonical_coordinates = self.load_NPHM_canonical_coordinates(timestep, mm_name=mm_name)
            mesh_trimesh = trimesh.Trimesh(mesh.vertices,
                                           mesh.faces,
                                           vertex_attributes={"canonical_coordinates": canonical_coordinates},
                                           process=False)
        else:
            mesh_trimesh = trimesh.Trimesh(mesh.vertices, mesh.faces, process=False)

        return mesh_trimesh

    def load_NPHM_canonical_coordinates(self, timestep: int, mm_name: str = 'NPHM') -> np.ndarray:
        canonical_coordinates_path = self.get_NPHM_canonical_coordinates_path(timestep, mm_name=mm_name)
        canonical_coordinates = np.load(canonical_coordinates_path)['arr_0']
        canonical_coordinates_quantizer = CanonicalCoordinatesQuantizer()
        canonical_coordinates = canonical_coordinates_quantizer.decode(canonical_coordinates)
        return canonical_coordinates

    def load_NPHM_expression_code(self, timestep: int, mm_name: str = 'NPHM') -> np.ndarray:
        expression_code_path = self.get_NPHM_expression_code_path(timestep, mm_name=mm_name)
        expression_code = np.load(expression_code_path)['arr_0']
        return expression_code

    # ==========================================================
    # Paths
    # ==========================================================
    # Folders
    # ----------------------------------------------------------

    # /sequences
    def get_sequences_folder(self) -> str:
        if self._relative:
            return "sequences"
        else:
            return f"{self._location}/sequences"

    # /sequences/$SEQUENCE
    def get_sequence_folder(self) -> str:
        return f"{self.get_sequences_folder()}/{self._sequence_name}"

    # /sequences/$SEQUENCE/timesteps
    def get_timesteps_folder(self) -> str:
        return f"{self.get_sequence_folder()}/timesteps"

    # /sequences/$SEQUENCE/timesteps/frame_$FRAME
    def get_timestep_folder(self, timestep: int) -> str:
        return f"{self.get_sequence_folder()}/timesteps/frame_{timestep:05d}"

    def get_image_folder_name(self) -> str:
        folder_name = "images" if self._downscale_factor == 1 else f"images-{self._downscale_factor}x"

        return folder_name

    # /sequences/$SEQUENCE/timesteps/frame_$FRAME/images
    def get_images_folder(self,
                          timestep: int) -> str:
        image_folder_name = self.get_image_folder_name()
        return f"{self.get_timestep_folder(timestep)}/{image_folder_name}"

    # ----------------------------------------------------------
    # Annotations
    # ----------------------------------------------------------

    def get_annotations_folder(self) -> str:
        return f"{self.get_sequence_folder()}/annotations"

    def get_color_correction_folder(self) -> str:
        return f"{self.get_annotations_folder()}/color_correction"

    def get_color_correction_path(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_color_correction_folder()}/{serial}.npy"

    def get_2d_landmarks_folder(self) -> str:
        return f"{self.get_annotations_folder()}/landmarks2D"

    def get_2d_landmarks_path(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_2d_landmarks_folder()}/PIPnet/{serial}.npy"

    def get_3d_landmarks_folder(self) -> str:
        return f"{self.get_annotations_folder()}/landmarks3D"

    def get_3d_landmarks_path(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_3d_landmarks_folder()}/{self._sequence_name}/PIPnet/{serial}.npy"

    def get_bounding_boxes_folder(self) -> str:
        return f"{self.get_annotations_folder()}/bbox"

    def get_bounding_boxes_path(self, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_bounding_boxes_folder()}/{serial}.npy"

    def get_3DMM_tracking_folder(self, mm_name: str) -> str:
        return f"{self.get_annotations_folder()}/tracking/{mm_name}"

    def get_NPHM_mesh_path(self, timestep: int, mm_name: str = 'NPHM') -> str:
        return f"{self.get_3DMM_tracking_folder(mm_name)}/{timestep:05d}_local_new.CTM"

    def get_NPHM_canonical_coordinates_path(self, timestep: int, mm_name: str = 'NPHM') -> str:
        return f"{self.get_3DMM_tracking_folder(mm_name)}/{timestep:05d}_canonical_vertices_uint16.npz"

    def get_NPHM_expression_code_path(self, timestep: int, mm_name: str = 'NPHM') -> str:
        return f"{self.get_3DMM_tracking_folder(mm_name)}/{timestep:05d}_ex_code.npz"

    # ----------------------------------------------------------
    # Images
    # ----------------------------------------------------------

    def get_image_file_name_format(self, has_downscale_factor: bool = False) -> str:
        image_folder_name = 'images'

        suffix = 'png'
        if has_downscale_factor:
            image_folder_name = image_folder_name + "-{f:}x"
            suffix = 'jpg'  # Downscaled images are stored as JPG

        return "{s:}/timesteps/frame_{t:05d}/" + image_folder_name + "/cam_{c:}." + suffix

    def get_relative_image_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:

        has_downscale_factor = self._downscale_factor > 1

        image_file_name_format = self.get_image_file_name_format(has_downscale_factor=has_downscale_factor)

        serial = self.cam_id_to_serial(cam_id_or_serial)
        format_args = {
            's': self._sequence_name,
            't': timestep,
            'c': serial
        }

        if has_downscale_factor:
            format_args['f'] = self._downscale_factor

        image_file_name = image_file_name_format.format(**format_args)

        return image_file_name

    def get_image_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        relative_image_path = self.get_relative_image_path(
            timestep,
            cam_id_or_serial
        )
        return f"{self.get_sequences_folder()}/{relative_image_path}"

    # ----------------------------------------------------------
    # Robust Matting
    # ----------------------------------------------------------

    def get_robust_matting_alpha_folder(self, timestep: int) -> str:
        alpha_map_folder_name = "alpha_map"
        return f"{self.get_timestep_folder(timestep)}/{alpha_map_folder_name}"

    def get_robust_matting_alpha_image_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_robust_matting_alpha_folder(timestep)}/cam_{serial}.png"

    # ----------------------------------------------------------
    # Calibration
    # ----------------------------------------------------------

    def get_calibration_folder(self) -> str:
        return self._participant_data_manager.get_calibration_folder()

    def get_calibration_result_path(self) -> str:
        return self._participant_data_manager.get_calibration_result_path()

    def get_calibration_run_config_path(self) -> str:
        return self._participant_data_manager.get_calibration_run_config_path()

    # ----------------------------------------------------------
    # COLMAP
    # ----------------------------------------------------------

    def get_colmap_folder(self, timestep: int) -> str:
        return f"{self.get_timestep_folder(timestep)}/colmap"

    def get_depth_maps_folder(self, timestep: int, n_cameras: int) -> str:
        return f"{self.get_colmap_folder(timestep)}/depth_maps_geometric/{n_cameras}"

    def get_normal_maps_folder(self, timestep: int, n_cameras: int) -> str:
        return f"{self.get_colmap_folder(timestep)}/normal_maps_geometric/{n_cameras}"

    def get_consistency_graphs_folder(self, timestep: int, n_cameras: int) -> str:
        return f"{self.get_colmap_folder(timestep)}/consistency_graphs/{n_cameras}"

    def get_depth_map_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE, n_cameras: int = 12) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        # return f"{self.get_depth_maps_folder(timestep, n_cameras)}/cam_{serial}.npz"
        return f"{self.get_depth_maps_folder(timestep, n_cameras)}/cam_{serial}.png"

    def get_normal_map_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE, n_cameras: int = 12) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        # return f"{self.get_normal_maps_folder(timestep, n_cameras)}/cam_{serial}.npz"
        return f"{self.get_normal_maps_folder(timestep, n_cameras)}/cam_{serial}.png"

    def get_consistency_graph_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE,
                                   n_cameras: int = 12) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_consistency_graphs_folder(timestep, n_cameras, )}/cam_{serial}.npz"

    def get_point_cloud_path(self, timestep, n_cameras: int = 12) -> str:
        return f"{self.get_colmap_folder(timestep)}/pointclouds/pointcloud_{n_cameras}.pcd"

    # ----------------------------------------------------------
    # Segmentation Mask
    # ----------------------------------------------------------

    def get_bisenet_segmentations_folder(self, timestep: int) -> str:
        return f"{self.get_timestep_folder(timestep)}/bisenet_segmentation_masks"

    def get_facer_segmentations_folder(self, timestep: int) -> str:
        # TODO: This is a temporary folder until we incorporated the facer script into the preprocessing pipeline
        # cluster_folder = self._location[:self._location.index('/doriath')]
        # return f"{cluster_folder}/angmar/sgiebenhain/facer_masks_v2/{self._participant_id:03d}/{self._sequence_name}/{timestep:05d}"
        # return f"{cluster_folder}/angmar/sgiebenhain/facer_masks/{self._participant_id:03d}/{self._sequence_name}/{timestep:05d}"
        return f"{self.get_timestep_folder(timestep)}/facer_segmentation_masks"

    def get_bisenet_segmentation_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        serial = self.cam_id_to_serial(cam_id_or_serial)
        return f"{self.get_bisenet_segmentations_folder(timestep)}/segmentation_cam_{serial}.png"

    def get_facer_segmentation_path(self, timestep: int, cam_id_or_serial: CAM_ID_SERIAL_TYPE) -> str:
        # TODO: This is a temporary path until we incorporated the facer script into the preprocessing pipeline
        serial = self.cam_id_to_serial(cam_id_or_serial)
        # return f"{self.get_facer_segmentations_folder(timestep)}/{serial}.png"
        return f"{self.get_facer_segmentations_folder(timestep)}/segmentation_cam_{serial}.png"


class FamudyParticipantDataFolder:

    def __init__(self, remote: bool = False):
        self._location = FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW if remote else FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW
        self._remote = remote

    def list_participants(self) -> List[int]:
        participants = []
        participant_regex = re.compile("0*(\d+)")
        for folder in Path(self._location).iterdir():
            match = participant_regex.match(folder.name)
            if match:
                participants.append(int(match.group(1)))
        participants = sorted(participants)

        return participants

    def list_calibrated_participants(self) -> List[int]:
        participant_ids = self.list_participants()
        calibrated_participant_ids = []
        for participant_id in participant_ids:
            data_manager = FamudyParticipantDataManager(participant_id, remote=self._remote)
            if data_manager.has_calibration_result():
                calibrated_participant_ids.append(participant_id)

        return calibrated_participant_ids

    def get_location(self) -> str:
        return self._location

    def get_processing_status_path(self) -> str:
        return f"{self._location}/processing_status.csv"

    def get_processing_status_flame_path(self) -> str:
        return f"{self._location}/processing_status_flame.csv"

    def load_processing_status(self) -> pd.DataFrame:
        return pd.read_csv(self.get_processing_status_path(), sep='\t', skiprows=1)

    def load_processing_status_flame(self) -> pd.DataFrame:
        return pd.read_csv(self.get_processing_status_flame_path(), sep='\t', skiprows=1)
