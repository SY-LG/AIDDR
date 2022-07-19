import threading,time,json,cv2,math,numpy as np

class chartLoaderThread(threading.Thread):
	def __init__(self,path,startTime,offset):
		threading.Thread.__init__(self)
		self.path=path
		self.startTime=startTime-offset/1000
	def run(self):
		self.quit=False
		self.startTime=time.perf_counter()
		self.background=cv2.resize(cv2.imread('./data/pictures/chartBG.png'),(600,600))
		self.xBias=75
		self.railWidth=150
		self.railLength=600
		self.yJudge=80
		for i in range(1,5):
			self.generateNote(self.background,i,self.railLength-self.yJudge,(255,255,255))
		self.loadChart(self.path)
		while time.perf_counter()<self.startTime:
			pass
		cv2.namedWindow('chart')
		while not self.quit:
			img=self.background.copy()
			for note in self.notes:
				if self.isLateNote(note["time"]):
					continue
				elif self.isEarlyNote(note["time"]):
					break
				y=self.railLength-self.spd*(note["time"]-(time.perf_counter()-self.startTime)*1000)+self.yJudge
				self.generateNote(img,note["rail"],y)
			cv2.imshow('chart',img)
			cv2.waitKey(1)
		cv2.destroyWindow('chart')
	def loadChart(self,chartPath):
		with open(chartPath,'r') as File:
			data=json.load(File)
		self.spd=data["spd"]
		self.notes=data["notes"]
	def isLateNote(self,t):
		return t<(time.perf_counter()-self.startTime)*1000
	def isEarlyNote(self,t):
		return t>=(time.perf_counter()-self.startTime)*1000+self.railLength/self.spd
	def generateNote(self,img,rail,y,color=(0,0,0)):
		downArrowPoints=[[-10,-20],[10,-20],[10,0],[20,0],[0,10],[-20,0],[-10,0]]
		arrawPoints=self.move(points=downArrowPoints,center=(self.xBias+self.railWidth*(rail-1),y),angle=math.pi*(0.25+0.5*rail),scale=3)
		arrow=np.array([[*arrawPoints]])
		cv2.fillPoly(img,arrow,color)
	def move(self,points,center=(0,0),angle=0,scale=1):
		movedPoints=[]
		for point in points:
			_x=point[0]*scale
			_y=point[1]*scale
			x=_y*math.sin(angle)+_x*math.cos(angle)
			y=_y*math.cos(angle)-_x*math.sin(angle)
			movedPoints.append([int(center[0]+x),int(center[1]+y)])
		return movedPoints