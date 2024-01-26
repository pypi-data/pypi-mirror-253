from typing import List, Tuple

import numpy as np

from famudy.env_data import FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW


class ExpressionAnimationManager:

    def __init__(self, expression_animation: str, skip: int = 1):
        cluster_folder = FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW[:FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW.index('/doriath')]
        self._expression_animation_folder = f"{cluster_folder}/doriath/sgiebenhain/{expression_animation}"
        self._skip = skip

        if "animation_4x4" in expression_animation:
            self._n_keyframes = None
            self._n_steps = 20

            self._timestep_matrix = [(step_1, step_2) for step_1 in range(self._n_steps) for step_2 in range(self._n_steps)]  # frame_id => (step_1, step_2)
            self._is_matrix = True
        else:
            self._n_keyframes = 20
            self._n_steps = 20
            self._is_matrix = False

    def get_n_steps(self) -> int:
        return self._n_steps

    def is_matrix(self) -> bool:
        return self._is_matrix

    def get_timestep_matrix(self) -> List[Tuple[int, int]]:
        return self._timestep_matrix

    def get_timesteps(self) -> List[int]:
        if self._is_matrix:
            timesteps = []
            timestep = 0
            for step_1 in range(self._n_steps):
                for step_2 in range(self._n_steps):
                    if step_1 % self._skip == 0 and step_2 % self._skip == 0:
                        timesteps.append(timestep)
                    timestep += 1
        else:
            timesteps = list(range(0, self._n_keyframes * self._n_steps, self._skip))
        # timesteps = Folder(self._expression_animation_folder).list_file_numbering("$_local_new.CTM", return_only_numbering=True)
        return timesteps

    def get_mesh_path(self, timestep: int) -> str:
        if self._is_matrix:
            step_1, step_2 = self._timestep_matrix[timestep]
            return f"{self._expression_animation_folder}/{step_1:05d}_{step_2:05d}_local_new.CTM"
        else:
            return f"{self._expression_animation_folder}/{timestep:05d}_local_new.CTM"

    def get_canonical_vertices_path(self, timestep: int) -> str:
        if self._is_matrix:
            step_1, step_2 = self._timestep_matrix[timestep]
            return f"{self._expression_animation_folder}/{step_1:05d}_{step_2:05d}_canonical_vertices_uint16.npz"
        else:
            return f"{self._expression_animation_folder}/{timestep:05d}_canonical_vertices_uint16.npz"

    def get_expression_codes_path(self):
        if self._is_matrix:
            return f"{self._expression_animation_folder}/latent_code_matrix.npy"
        else:
            return f"{self._expression_animation_folder}/nphm_animation_codes.npy"

    def load_expression_code(self, timestep: int) -> np.ndarray:
        if self._is_matrix:
            step_1, step_2 = self._timestep_matrix[timestep]
            expression_codes = np.load(self.get_expression_codes_path())
            lat_rep_expr = expression_codes[step_1][step_2]
        else:
            expression_codes = np.load(self.get_expression_codes_path())
            N_KEYFRAMES = 20
            N_STEPS = 20
            keyframe_1 = (int(timestep / N_STEPS)) % N_KEYFRAMES
            keyframe_2 = (keyframe_1 + 1) % N_KEYFRAMES
            lat_rep_expr1 = expression_codes[keyframe_1]
            lat_rep_expr2 = expression_codes[keyframe_2]
            step = timestep - keyframe_1 * N_STEPS
            assert step >= 0
            assert step < N_STEPS

            lat_rep_expr = lat_rep_expr1 * (N_STEPS - step) / N_STEPS + lat_rep_expr2 * step / N_STEPS

        return lat_rep_expr
