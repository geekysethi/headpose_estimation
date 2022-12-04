import cv2
from headpose_estimation import Headpose
import numpy as np

if __name__ == "__main__":

	headpose = Headpose()
	image_path = '/Users/ashish/Desktop/projects/HeadPoseEstimation-WHENet/Sample/random_internet_selfie.jpg'
	img = cv2.imread(image_path)

	headpose.run(img)
