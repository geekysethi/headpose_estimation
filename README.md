# State of art the Head Pose Estimation in Tensorflow2 

This repository includes:
- ["WHENet: Real-time Fine-Grained Estimation for Wide Range Head Pose" (BMVC 2020).](https://www.bmvc2020-conference.com/assets/papers/0907.pdf) adapted from the [original source code](https://github.com/Ascend-Research/HeadPoseEstimation-WHENet).


- [RetinaFace: Single-stage Dense Face Localisation in the Wild](https://arxiv.org/abs/1905.00641) adapted from https://github.com/StanislasBertrand/RetinaFace-tf2.





<img src=images/output.png height="220"/> 



## Install

You can install this repository with pip (requires python>=3.6);

```
pip install headpose_estimation
```

```bash
pip install git+https://github.com/geekysethi/headpose_estimation
```

You can also install with the `setup.py`

##  With Face Detection
To perform detection you can simple use the following lines:

```python
import cv2
from headpose_estimation import Headpose
headpose = Headpose()
img = cv2.imread("path_to_im.jpg")
detections,image = headpose.run(img)
```

This will return a list of dictionary which looks like this `[{'bbox': [xmin, ymin, xmax, ymax], 'yaw': yaw_value, 'pitch': pitch_value, 'roll': roll_value}`


##  Without Face Detection
To perform detection you can simple use the following lines:

```python
import cv2
from headpose_estimation import Headpose
headpose = Headpose(face_detection=False)
imgcrop = cv2.imread("path_to_im.jpg")
detections,image = headpose.run(imgcrop)
```

In this case it will return a list of dictionary which looks like this `[{'yaw': yaw_value, 'pitch': pitch_value, 'roll': roll_value}`

## Dependncies
* EfficientNet https://github.com/qubvel/efficientnet
