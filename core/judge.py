#修改了camera，对应的在camera2，一部分判断在camera2里

# camera.py will call judgeFrame in each frame.
# you need to judge what the player should do and how he's doing.
# There will be a param that tells the start time.
# return format: (indexOfNote,Judegement)
# indexOfNote is the index of note in the json file. If no note is judged in that frame, return None
# Judgement can be None,"Perfect","Good","Bad" or "Miss"
# Judge one note per frame is OK (I guess), since if two notes should be judged at the same time,
# judging them in two frames should not make a big difference.


import mediapipe as mp



def judgeFrame(frame,flag):
    mpPose = mp.solutions.pose 
    pose = mpPose.Pose(static_image_mode=False, smooth_landmarks=True,min_detection_confidence=0.5, min_tracking_confidence=0.5)
     
    mpDraw = mp.solutions.drawing_utils
    results = pose.process(frame)
    lmList = []
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy, lm.z])

    return judge(flag,lmList)


#分动作。可以再增减
#0：左手向左，1：右手向右
#2：左脚向左，3：右脚向右
def judge(flag,lmList):
    if flag==0 :
        return (lmList[15][1]-lmList[11][1])>(lmList[11][1]-lmList[12][1])
    elif flag==1 :
        return (lmList[11][1]-lmList[12][1])>(lmList[12][1]-lmList[16][1])
    elif flag==2 :
        return (lmList[27][1]>lmList[11][1])
    elif flag==3 :
        return (lmList[28][1]<lmList[12][1])



