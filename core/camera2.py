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
		pd.DataFrame(res).to_csv("music.csv")
		pos=0#指代第几行

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

			while((time.perf_counter()-self.startTime)>=res[pos]-300 and (time.perf_counter()-self.startTime)<=res[pos][2]+300):#判断移动一部分到这里，这里是什么时候应该开始判断及结果
				judged=1
				bad=judge.judgeFrame(frame,res[pos][1])
				if bad :
					break
				while((time.perf_counter()-self.startTime)>=res[pos]-160 and (time.perf_counter()-self.startTime)<=res[pos][2]+160):
					good =judge.judgeFrame(frame,res[pos][1])
					if good :
						break
					while((time.perf_counter()-self.startTime)>=res[pos]-80 and (time.perf_counter()-self.startTime)<=res[pos][2]+80):
						perfect=judge.judgeFrame(frame,res[pos][1])
						if perfect:
							break

			if judged:
				pos+=1
				score=perfect+good+bad+1
				miss=not (perfect or good or bad)
				results.append = [{'score':score,'perfect':perfect,'good':good,'bad':bad,'miss':miss}]

		with open ('results.csv','w',encoding='utf-8') as fp:
			writer =csv.DictWriter(fp,['score','perfect','good','bad','miss'])
			writer.writeheader()
			writer.writerows(results)

		camera.release()
		cv2.destroyAllWindows()

