
def judge(flag,lmList):
    if flag==0 :#"hand_left"
        return (lmList[15][1]-lmList[11][1])>(lmList[11][1]-lmList[12][1])
    elif flag==1 :#"hand_right"
        return (lmList[11][1]-lmList[12][1])>(lmList[12][1]-lmList[16][1])
    elif flag==2 :#"foot_left"
        return (lmList[27][1]>lmList[11][1])
    elif flag==3 :#"foot_right"
        return (lmList[28][1]<lmList[12][1])


def score(self,results,img,poses=[],weight=1):
    #results是姿态识别模型的结果
    #img就是原图，其实我需要的只是每一帧图像的长宽，所以传给我[x,y]也行，可以改
    #poses是bool型列表，表示一个动作由几个基本动作组成，比如poses[1]=1的话就是有手向右伸的动作
    #weight权值，就是之前讲的如果一个动作难度较高，我们可以适当增加得分，令weight=2，默认是1
    self.lmList = []
    if results.pose_landmarks:#这边if是判断是否检测到结果，如果另一位小哥判断过的话可删，直接进入for循环
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            self.lmList.append([id, cx, cy])

    self.final_score=0
    for i in range (4):#计算每一个小动作是否得分
        if(poses[i]):
            self.final_score+= judge(i,self.lmList)

    return (self.final_score*weight)
