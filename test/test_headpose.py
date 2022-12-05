import cv2
from headpose_estimation import Headpose
import numpy as np

if __name__ == "__main__":

	headpose = Headpose()
	image_path = '/Users/ashish/Desktop/projects/HeadPoseEstimation-WHENet/Sample/random_internet_selfie.jpg'
	img = cv2.imread(image_path)

	output,image = headpose.run(img)
	print(output)

	cv2.imwrite("output.png",image)
	# cv2.imshow("image",image)
	# cv2.waitKey()
	# cv2.destroyAllWindows()