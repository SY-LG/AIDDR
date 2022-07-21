import threading,cv2,time
from core import judge
class cameraThread(threading.Thread):
	def __init__(self,path,startTime):
		threading.Thread.__init__(self)
		self.quit=False
		self.path=path
		self.startTime=startTime
		self.judger=judge.judger(self.path,self.startTime)
	def run(self):
		camera=cv2.VideoCapture(0)
		while time.perf_counter()<self.startTime:
			pass
		cv2.namedWindow('camera')
		showPos=[(450,50),(50,50),(50,450),(450,450)]
		i=0
		showList=[]
		self.finalResult={"Score":0,"total":0,"Perfect":0,"Good":0,"Bad":0,"Miss":0}
		while camera.isOpened() and not self.quit:
			t=(time.perf_counter()-self.startTime)*1000
			ret,frame=camera.read()
			if ret:
				frame=cv2.flip(frame,1)
				frame,result=self.judger.judgeFrame(frame)
				if result:
					showList.append(result)
					self.finalResult[result[1]]+=1
					self.finalResult["total"]+=1
				for i,showObject in enumerate(showList):
					if t-showObject[2]<500:
						break
				showList=showList[i:]
				for showObject in showList:
					cv2.putText(frame, showObject[1], showPos[showObject[0]], cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
				cv2.imshow('camera',frame)
				cv2.waitKey(1)
		camera.release()
		cv2.destroyAllWindows()
		self.finalResult["Score"]=100000*(self.finalResult["Perfect"]+self.finalResult["Good"]*0.5+self.finalResult["Bad"]*0.3)