import threading,cv2,time
from core import judge
class cameraThread(threading.Thread):
	def __init__(self,path,startTime):
		threading.Thread.__init__(self)
		self.quit=False
		self.path=path
		self.startTime=startTime
	def run(self):
		camera=cv2.VideoCapture(0)
		judger=judge.judger(self.path)
		while time.perf_counter()<self.startTime:
			pass
		cv2.namedWindow('camera')
		while camera.isOpened() and not self.quit:
			ret,frame=camera.read()
			if ret:
				cv2.imshow('camera',frame)
				cv2.waitKey(1)
		camera.release()
		cv2.destroyAllWindows()
