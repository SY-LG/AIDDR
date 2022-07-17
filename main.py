from mttkinter import mtTkinter as tkinter
import json,time,numpy as np
import camera,chartLoader,music
#from PIL import Image,ImageTk

# def image_CV2ToTk(img):
# 	image=Image.fromarray(np.uint8(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)))
# 	return ImageTk.PhotoImage(image=image)

def start():
	hideAll()# tkinter window would stuck here, reason unknown! (bug not fatal)
	time.sleep(0.5)
	cameraThread=camera.cameraThread()
	chartThread=chartLoader.chartLoaderThread()
	musicThread=music.musicThread(volume=volumeScale.get())
	cameraThread.start()
	chartThread.start()
	musicThread.start()
	time.sleep(5)
	cameraThread.quit=True
	chartThread.quit=True
	musicThread.quit=True
	time.sleep(1)
	cameraThread.join()
	chartThread.join()
	musicThread.join()
	showMenu()

def option():
	hideAll()
	showMenu()
	showOption()

win=tkinter.Tk()
win.title('AIDDR')
win.geometry('1400x800')

startButton=tkinter.Button(win,command=start,text='Start')
optionButton=tkinter.Button(win,command=option,text='Option')
exitButton=tkinter.Button(win,command=lambda : win.destroy(),text='Exit')

volumeScale=tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL)
volumeScale.set(100)
volumeLabel=tkinter.Label(win,text='volume')

offsetScale=tkinter.Scale(win,from_=-100,to=100,orient=tkinter.HORIZONTAL)
offsetScale.set(0)
offsetLabel=tkinter.Label(win,text='offset')

def showMenu():
	startButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)
	optionButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)
	exitButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)

def hideMenu():
	startButton.pack_forget()
	optionButton.pack_forget()
	exitButton.pack_forget()

def showOption():
	volumeScale.pack(anchor='s',side=tkinter.TOP)
	volumeLabel.pack(anchor='s',side=tkinter.TOP)
	offsetScale.pack(anchor='s',side=tkinter.TOP)
	offsetLabel.pack(anchor='s',side=tkinter.TOP)

def hideOption():
	volumeScale.pack_forget()
	volumeLabel.pack_forget()
	offsetScale.pack_forget()
	offsetLabel.pack_forget()

def hideAll():
	hideMenu()
	hideOption()

showMenu()
win.mainloop()