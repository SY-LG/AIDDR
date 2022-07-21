import time,json,mediapipe as mp,cv2
class judger:
	def __init__(self,path,startTime):
		with open(path,'r') as File:
			self.notes=json.load(File).get('notes')
		for i in range(len(self.notes)):
			self.notes[i]["num"]=i
		self.startTime=startTime
		self.pose=mp.solutions.pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
		self.status=[[False,]*12,]*4
	def judgeFrame(self,frame):
		self.frame=frame
		self.updateStatus()
		motion=[self.judgeStatus(i) for i in range(4)]
		return (self.frame,self.judgeMotion(motion))
	def updateStatus(self):
		self.landmarks=self.getLandmarks()
		for i in range(4):
			self.status[i]=[*self.status[i][1:],self.judge(i)]
	def getLandmarks(self):
		_=self.pose.process(cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)).pose_landmarks
		if _:
			mp.solutions.drawing_utils.draw_landmarks(self.frame,_,mp.solutions.pose.POSE_CONNECTIONS)
			return _.landmark
		else:
			# no object detected
			return None
	def judgeStatus(self,i):
		return self.bufcnt(self.status[i][-6:],True,2) and self.bufcnt(self.status[i][:-6],False,2)
		# return self.status[i] and not self.statusLast[i]
	def bufcnt(self,conditions,targetCondition,targetNum):
		cnt=0
		for condition in conditions:
			if condition==targetCondition:
				cnt+=1
			else:
				cnt=0
			if cnt==targetNum:
				return True
		return False
	def judgeMotion(self,motion):
		timeBad=1000
		timeGood=500
		timePerfect=200
		t=(time.perf_counter()-self.startTime)*1000
		for i,note in enumerate(self.notes):
			note=self.notes[i]
			if t>note["time"]+timeBad:
				self.notes.pop(i)
				return (note["rail"]-1,"Miss",t)
			elif t<note["time"]-timeBad:
				return None
			elif motion[note["rail"]-1]:
				self.notes.pop(i)
				if t>note["time"]-timePerfect and t<note["time"]+timePerfect:
					return (note["rail"]-1,"Perfect",t)
				elif t>note["time"]-timeGood and t<note["time"]+timeGood:
					return (note["rail"]-1,"Good",t)
				else:
					return (note["rail"]-1,"Bad",t)
		else:
			return None
	def judge(self,flag):
		if self.landmarks is None:
			return False
		if flag==0:
			return self.landmarks[15].x-self.landmarks[11].x>self.landmarks[11].x-self.landmarks[12].x
		elif flag==1:
			return self.landmarks[11].x-self.landmarks[12].x<self.landmarks[12].x-self.landmarks[16].x
		elif flag==2:
			return self.landmarks[28].x<self.landmarks[12].x
		elif flag==3:
			return self.landmarks[27].x>self.landmarks[11].x
