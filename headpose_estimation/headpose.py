import os
from pathlib import Path
from typing import overload

import cv2
import numpy as np

from headpose_estimation.face_detector.retinaface import RetinaFace

from .utils import draw_axis
from .whenet import WHENet


class Headpose():

	def __init__(self,face_detection = True,draw = True) -> None:
		
		self.face_detection = face_detection
		self.draw = draw
		self.detector = RetinaFace()
		dirname = os.path.dirname(__file__)
		print(dirname)
		model_path = Path(os.path.join(dirname, "WHENet.h5"))
		self.headpose = WHENet(snapshot=model_path)



	def draw_bbox(self,image,bboxes):

		if bboxes is not None:
			for i in range(bboxes.shape[0]):
				box = bboxes[i].astype(int)
				color = (0, 255, 0)
				cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), color, 2)


	def detect_faces(self,image):
		bboxes = []
		bboxes_dict = self.detector.detect_faces(image, 0.9)
		for k,current_bbox in bboxes_dict.items():
			bboxes.append(current_bbox["facial_area"])
		return bboxes
	
	def _pad_bbox(self,image,bbox):

		x_min, y_min, x_max,y_max = bbox
		y_min = max(0, y_min - abs(y_min - y_max) / 10)
		y_max = min(image.shape[0], y_max + abs(y_min - y_max) / 10)
		x_min = max(0, x_min - abs(x_min - x_max) / 5)
		x_max = min(image.shape[1], x_max + abs(x_min - x_max) / 5)
		x_max = min(x_max, image.shape[1])

		return [x_min, y_min, x_max,y_max]


	@overload
	def detect_headpose(self,image):

		img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		img_rgb = cv2.resize(img_rgb, (224, 224))
		img_rgb = np.expand_dims(img_rgb, axis=0)

		yaw, pitch, roll = self.headpose.get_angle(img_rgb)
		yaw, pitch, roll = np.squeeze([yaw, pitch, roll])


		return yaw, pitch,roll

	def detect_headpose(self,image,padded_bbox):

		x_min, y_min, x_max,y_max = padded_bbox

		img_rgb = image[int(y_min):int(y_max), int(x_min):int(x_max)]
		img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
		img_rgb = cv2.resize(img_rgb, (224, 224))
		img_rgb = np.expand_dims(img_rgb, axis=0)
		yaw, pitch, roll = self.headpose.get_angle(img_rgb)
		yaw, pitch, roll = np.squeeze([yaw, pitch, roll])


		return yaw, pitch,roll


	def run(self,image):
		
		pass
		final_output = []
		if(self.face_detection):
			bboxes = self.detect_faces(image)
			for current_bbox in bboxes:

				padded_bbox = self._pad_bbox(image,current_bbox)
				yaw,pitch,roll = self.detect_headpose(image,padded_bbox)

				final_output.append({"bbox":np.array(current_bbox),"yaw":yaw,"pitch": pitch,"roll": roll})
				if(self.draw):
					x_min, y_min, x_max,y_max = padded_bbox
					cv2.rectangle(image,(int(x_min),int(y_min)),(int(x_max),int(y_max)),(0,255,0),2)
					draw_axis(image, yaw, pitch, roll, tdx=(x_min+x_max)/2, tdy=(y_min+y_max)/2, size = abs(x_max-x_min)//2 )

				
			if(self.draw):
				return final_output,image
			return final_output

		else:

			yaw,pitch,roll = self.detect_headpose(image)

			final_output.append({"yaw":yaw,"pitch": pitch,"roll": roll})
			if(self.draw):
				height,width,_ = image.shape
				x_min, y_min, x_max,y_max = 0,0,width,height
				draw_axis(image, yaw, pitch, roll, tdx=(x_min+x_max)/2, tdy=(y_min+y_max)/2, size = abs(x_max-x_min)//2 )				
				return final_output,image

			return final_output







if __name__ == "__main__":

	headpose = Headpose()
	image_path = '/Users/ashish/Desktop/projects/HeadPoseEstimation-WHENet/Sample/random_internet_selfie.jpg'
	img = cv2.imread(image_path)

	output,image = headpose.run(img)
	cv2.imshow("image",image)
	cv2.waitKey()
	cv2.destroyAllWindows()