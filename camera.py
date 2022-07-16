import threading,cv2
class cameraThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.quit=False
	def run(self):
		camera=cv2.VideoCapture(0)
		cv2.namedWindow('camera')
		while camera.isOpened() and not self.quit:
			ret,frame=camera.read()
			if ret:
				cv2.imshow('camera',frame)
				cv2.waitKey(1)
		camera.release()
		cv2.destroyAllWindows()
		return