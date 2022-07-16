import threading,time,json,cv2,math,numpy as np

class chartLoaderThread(threading.Thread):#params inside needs adjustment
	def run(self):
		self.quit=False
		self.startTime=time.perf_counter()
		self.background=cv2.imread('./chartBG.png')
		self.railLength=1000
		loadChart('./chart1.json')
		cv2.namedWindow('chart')
		while not self.quit:
			img=self.background.copy()
			for note in notes:
				if isLateNote(note["time"]):
					continue
				elif isEarlyNote(note["time"]):
					break
				y=self.railLength-self.spd*(time.perf_counter()-self.startTime)
				generateNote(img,note["type"],y)
			cv2.imshow('chart',img)
			cv2.waitKey(1)
		cv2.destroyWindow('chart')
		return
	def loadChart(self,chartPath):
		with open(chartPath,'r') as File:
			data=json.load(File)
		self.spd=data["spd"]
		self.notes=data["notes"]
	def isLateNote(t):
		return t<(time.perf_counter()-self.startTime)*1000
	def isEarlyNote(t):
		return t>=(time.perf_counter()-self.startTime)*1000+self.railLength/self.spd
	def generateNote(img,rail,y,color=(0,0,0)):
		downArrowPoints=[[-10,-20],[10,-20],[10,0],[20,0],[0,10],[-20,0],[-10,0]]
		xBias=10
		railWidth=30
		arrawPoints=move(points=downArrowPoints,center=(xBias+railWidth*(rail-1),y),angle=math.pi*(0.25+0.5*rail))
		arrow=np.array([[*arrawPoints]])
		cv2.fillPoly(img,arrow,color)
	def move(points,center=(0,0),angle=0):
		movedPoints=[]
		for point in points:
			_x=point[0]
			_y=point[1]
			x=_y*math.sin(angle)+_x*math.cos(angle)
			y=_y*math.cos(angle)-_x*math.sin(angle)
			movedPoints.append([int(center[0]+x),int(center[1]+y)])
		return movedPoints
		

def move(points,center=(0,0),angle=0,scale=1):
	movedPoints=[]
	for point in points:
		_x=point[0]*scale
		_y=point[1]*scale
		x=_y*math.sin(angle)+_x*math.cos(angle)
		y=_y*math.cos(angle)-_x*math.sin(angle)
		movedPoints.append([int(center[0]+x),int(center[1]+y)])
	return movedPoints
def generateNote(img,rail,y,color=(0,0,0)):
	downArrowPoints=[[-10,-20],[10,-20],[10,0],[20,0],[0,20],[-20,0],[-10,0]]
	xBias=70
	railWidth=150
	arrawPoints=move(points=downArrowPoints,center=(xBias+railWidth*(rail-1),y),angle=math.pi*(0.25+0.5*rail),scale=3)
	arrow=np.array([[*arrawPoints]])
	cv2.fillPoly(img,arrow,color)
if __name__ == '__main__':
	img=cv2.imread('./chartBG.png')
	img=cv2.resize(img,(600,600))
	generateNote(img,1,100)
	cv2.circle(img,(75,100),5,(0,255,0))
	generateNote(img,2,200)
	cv2.circle(img,(225,200),5,(0,255,0))
	generateNote(img,3,500)
	cv2.circle(img,(375,500),5,(0,255,0))
	generateNote(img,4,300)
	cv2.circle(img,(525,300),5,(0,255,0))
	cv2.imshow('i',img)
	cv2.waitKey(0)
	cv2.destroyWindow('i')
