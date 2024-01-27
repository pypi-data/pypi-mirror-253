# famudy-data

Light-weight Python access to multi-view data from NeRSemble dataset.  
The main data resides on the cluster in `/cluster/doriath/tkirschstein/data/famudy/full`

### 1. Installation

```shell
pip install git+ssh://git@github.com/tobias-kirschstein/famudy-data.git
```
### 2. Setup
Create a file in your home directory:
`~/.config/famudy/.env`  
with content:
```shell
FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW="/cluster/doriath/tkirschstein/data/famudy/full"
```
Additionally, if you mounted rohan locally and want to access the data from your local machine, use another environment variable:
```shell
FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW="<<<PATH_TO_LOCAL_ROHAN_MOUNT>>>/cluster/doriath/tkirschstein/data/famudy/full"
```
For example, using WSL2 on Wndows with rohan mounted into `/mnt/rohan`,  `<<<PATH_TO_LOCAL_ROHAN_MOUNT>>>` would be `//wsl.localhost/Ubuntu/mnt/`.

# Usage

```python
from famudy.data import FamudySequenceDataManager

participant_id = ...
sequence_name = ...

data_manager = FamudySequenceDataManager(participant_id, sequence_name, downscale_factor=2)
```

### Images
```python
timestep = ...
cam_id = ...

image = data_manager.load_image(timestep, cam_id)
```

### Pointclouds, Depth maps or Normal maps
```python
timestep = ...
cam_id = ...

depth_map = data_manager.load_depth_map(timestep, cam_id, n_cameras=16)
normal_map = data_manager.load_normal_map(timestep, cam_id, n_cameras=16)
points, colors, normals = data_manager.load_point_cloud(timestep, n_cameras=16)
# n_cameras=16 indicates that COLMAP was ran on all 16 cameras
```

### Background masks
```python
timestep = ...
cam_id = ...

alpha_map = data_manager.load_robust_matting_alpha_image(timestep, cam_id)
```

### Camera extrinsics/intrinsics
Extrinsics are in `OpenCV` format and `world2cam`:
```python
world_2_cam_poses = data_manager.load_calibration_result().params_result.get_poses()
intrinsics = data_manager.load_calibration_result().params_result.get_intrinsics()
```
Note: the intrinsics is given wrt to the full resolution recordings (2200x3208). However, in the interest of storage, images and depth maps are downscaled by a factor of 2 (yielding 1100x1604). Hence, the intrinsics most likely needs to be rescaled as well by `intrinsics.rescale(0.5)`.

### Segmentation masks
```python
timestep = ...
cam_id = ...

segmentation_mask = data_manager.load_bisenet_segmentation_mask(timestep, cam_id)
```

### Landmarks
The most reliable landmarks are those detected from the front camera (serial = `222200037` / cam_id = `8`)
```python
cam_id = ...
landmarks = data_manager.load_2d_landmarks(cam_id)
```

### FLAME tracking
```python
flame_params = data_manager.load_3DMM_tracking("FLAME2023_v2")
```
