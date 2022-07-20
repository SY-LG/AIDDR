import pandas as pd
import json
import threading
import cv2
import time
import judge
class cameraThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.quit=False
	def run(self):
		# 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
		f = open("music.json", encoding="utf-8")#解析文件，还需要知道具体哪个音乐文件
		file = json.load(f)
		res = []
		for i in file["notes"]:
			res.append(i)
		pd.DataFrame(res).to_csv("music.csv")
		pos=0#指代第几行

		camera=cv2.VideoCapture(0)
		cv2.namedWindow('camera')
		while camera.isOpened() and not self.quit:
			ret,frame=camera.read()
			if ret:
				cv2.imshow('camera',frame)
				cv2.waitKey(1)

			perfect=0
			good=0
			bad=0
			judged=0

			while(time.time()>=res[pos]-300 and time.time()<=res[pos][2]+300):#判断移动一部分到这里，这里是什么时候应该开始判断及结果
				judged=1
				bad=judge.judgeFrame(frame,res[pos][1])
				if bad :
					break
				while(time.time()>=res[pos]-160 and time.time()<=res[pos][2]+160):
					good =judge.judgeFrame(frame,res[pos][1])
					if good :
						break
					while(time.time()>=res[pos]-80 and time.time()<=res[pos][2]+80):
						perfect=judge.judgeFrame(frame,res[pos][1])
						if perfect:
							break
			if judged:
				pos+=1
				result=0
				if bad:
					result=1
				elif good:
					resukt=2
				elif perfect:
					result=3
			#可以另外定义一个函数传递result
			#0:miss,1:bad,2:good,3:perfect

		camera.release()
		cv2.destroyAllWindows()
