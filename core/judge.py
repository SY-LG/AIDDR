import time,json
class judger:
    def __init__(self,path):
        with open(path,'r') as File:
            self.notes=json.load(File).get('notes')
    def judgeFrame(frame):
        pass

# camera.py will call judgeFrame in each frame.
# you need to judge what the player should do and how he's doing.
# There will be a param that tells the start time.
# return format: (indexOfNote,Judegement)
# indexOfNote is the index of note in the json file. If no note is judged in that frame, return None
# Judgement can be None,"Perfect","Good","Bad" or "Miss"
# Judge one note per frame is OK (I guess), since if two notes should be judged at the same time,
# judging them in two frames should not make a big difference.

#1.使用就是import 文件名（可以重新命名我没起名字），每一帧要判断的时候调用 文件名.score(各种参数，下有说明)
#2.这个加了z方向的变化，动作更多了些，不知道能不能z方向识别准确，也许可以试试
#3.有考虑到比如手遮挡了肩膀那么肩膀处的关键点是否能识别出来的问题，我看一些大佬实现识别的视频里，即使遮挡住身体的某些部分，比如手挡住了脸之类，
#脸上的关键点也还是存在的，所以没有做处理，暂时不知道是否有影响

#分动作。可以再增减
#0：左手向左，1：右手向右
#2：左脚向左，3：右脚向右
#4：左脚左前，5：右脚右前
#6：左脚左后，7：右脚右后
#8：左脚向前，9：右脚向前
#10：左脚向后，11：右脚向后
#12：左手向上，13：右手向上
#14：左手横胸前，15：右手横胸前
def judge(flag,lmList):
    if flag==0 :
        return (lmList[15][1]-lmList[11][1])>(lmList[11][1]-lmList[12][1])
    elif flag==1 :
        return (lmList[11][1]-lmList[12][1])>(lmList[12][1]-lmList[16][1])
    elif flag==2 :
        return (lmList[27][1]>lmList[11][1])
    elif flag==3 :
        return (lmList[28][1]<lmList[12][1])
    elif flag==4 :
        return (lmList[27][3]<lmList[23][3]) and (lmList[27][1]>lmList[11][1])
    elif flag==5 :
        return (lmList[28][3]<lmList[24][3]) and (lmList[12][1]>lmList[12][1])
    elif flag==6 :
        return (lmList[27][3]>lmList[23][3]) and (lmList[27][1]>lmList[11][1])
    elif flag==7 :
        return (lmList[28][3]>lmList[24][3]) and (lmList[12][1]>lmList[12][1])
    elif flag==8 :
        return (lmList[27][3]<lmList[23][3])
    elif flag==9 :
        return (lmList[28][3]<lmList[24][3])
    elif flag==10 :
        return (lmList[27][3]>lmList[23][3])
    elif flag==11 :
        return (lmList[28][3]>lmList[24][3])
    elif flag==12 :
        return (lmList[15][2]>lmList[1][2])
    elif flag==13 :
        return (lmList[16][2]>lmList[4][2])
    elif flag==14 :
        return (lmList[15][3]<lmList[11][3]) and (lmList[11][1]>lmList[15][1])
    elif flag==15 :
        return (lmList[16][3]<lmList[12][3]) and (lmList[16][1]>lmList[12][1])


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
            self.lmList.append([id, cx, cy, lm.z])

    self.final_score=0
    for i in range (16):#计算每一个小动作是否得分
        if(poses[i]):
            self.final_score+= judge(i,self.lmList)

    return (self.final_score*weight)
