import pandas as pd
import json
import threading
import cv2
import time
import csv

import sys
sys.path.append('D:\learning\python\work\AIDDR-main\core')
import judge

class cameraThread(threading.Thread):
	def __init__(self,startTime,path):
		threading.Thread.__init__(self)
		self.quit=False
		self.startTime=startTime
		self.path=path
	def run(self):
		# 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
		f = open(self.path, encoding="utf-8")
		file = json.load(f)
		res = []
		for i in file["notes"]:
			res.append(i)
		pos=1#指代第几行

		results=[]

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
			miss=1
			judged=0

			while((time.perf_counter()-self.startTime)*1000>=res[pos]["time"]-300 ):
				pos+=1
				flag=0
				while ((time.perf_counter()-self.startTime)*1000<=res[pos]["time"]+300) :
					judged=1
					flag=1
					bad=judge.judgeFrame(frame=frame,flag=res[pos]["rail"])
					if bad :
						break
					while((time.perf_counter()-self.startTime)*1000>=res[pos]["time"]-160 and (time.perf_counter()-self.startTime)*1000<=res[pos]["time"]+160):
						good =judge.judgeFrame(frame,res[pos]["rail"])
						if good :
							break
						while((time.perf_counter()-self.startTime)*1000>=res[pos]["time"]-80 and (time.perf_counter()-self.startTime)*1000<=res[pos]["time"]+80):
							perfect=judge.judgeFrame(frame,res[pos]["rail"])
							if perfect:
								break
				if flag:
					break

			if judged:
				pos+=1
				score=perfect+good+bad+1
				miss=not (perfect or good or bad)
				#结果？

		camera.release()
		cv2.destroyAllWindows()

