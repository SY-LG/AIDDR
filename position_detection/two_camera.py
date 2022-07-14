#这是关于把一个摄像头的窗口分成左右两个的代码，如果我们要做双人pk的话也许可以用到，
#我猜（我不大懂），如果要实现双人联机的话，也许可以用mqtt或者socket模块实现，但当然在一个电脑上比较简单了（。

import cv2
 
 
cv2.namedWindow("left")
cv2.namedWindow("right")
camera = cv2.VideoCapture(0)
 
# 设置分辨率 左右摄像机同一频率，同一设备ID；左右摄像机总分辨率1280x720；分割为两个640x720、640x720
# 上面是我的电脑的分辨率，电脑的分辨率可以在自带相机的设置里看
camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

 
while True:
    ret, frame = camera.read()
    # 裁剪
    if ret:
        left_frame = frame[0:720, 0:640]
        right_frame = frame[0:720, 640:1280]
 
        cv2.imshow("left", left_frame)
        cv2.imshow("right", right_frame)
 
    key = cv2.waitKey(1)
    if key == ord(" "):
        break

camera.release()
cv2.destroyWindow("left")
cv2.destroyWindow("right")
