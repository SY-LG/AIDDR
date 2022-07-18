from mttkinter import mtTkinter as tkinter
import json,time,numpy as np
from core import camera,chartLoader,music

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

def options():
	hideAll()
	showOptions()
	showBack()

def help():
	hideAll()
	showHelp()
	showBack()

def credits():
	hideAll()
	showCredits()
	showBack()

def back():
	hideAll()
	showMenu()

win=tkinter.Tk()
win.title('AIDDR')
win.geometry('1400x800')

startButton=tkinter.Button(win,command=start,text='Start')
optionsButton=tkinter.Button(win,command=options,text='Options')
helpButton=tkinter.Button(win,command=help,text='Help')
creditsButton=tkinter.Button(win,command=credits,text='Credits')
exitButton=tkinter.Button(win,command=lambda : win.destroy(),text='Exit')

backButton=tkinter.Button(win,command=back,text='Back')

optionsBanner=tkinter.Label(win,text='Options',font=('Arial', 15))

volumeScale=tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL)
volumeScale.set(100)
volumeLabel=tkinter.Label(win,text='volume')

offsetScale=tkinter.Scale(win,from_=-100,to=100,orient=tkinter.HORIZONTAL)
offsetScale.set(0)
offsetLabel=tkinter.Label(win,text='offset')

helpBanner=tkinter.Label(win,text='Help of AIDDR',font=('Arial', 15))
helpContent=tkinter.Label(win,text='''What is AIDDR?\n
	DDR(Dance Dance Revolution) is a series of video games made by Konami
	 in which players step on arrows on a large pad or mat to match the arrows on screen.
	 The arrows are in time with the music.
	 Because players are moving themselves along to the music,
	 they look like they are dancing.\n
	With Artificial Intelligence, we can now have fun at home.
	 Instead of a large pad, all you need is a camera.
	 Artificial Intelligence will judge your motion and score accordingly.\n
	How to play AIDDR?\n
	Stretch out your arms and legs as the arrows reach the bottom of the screen.
	For example, if it's a top-left arrow, top means you should use your arm,
	 and left means you should use your left arm/leg.
	 So, in this case, just stretch out your left arm
	 when that arrow reach the bottom of the screen.
	''')

creditsBanner=tkinter.Label(win,text='AIDDR\n@AI001-AIDDR team 2022',font=('Arial', 15))
creditsContent=tkinter.Label(win,text='Team members:\nSYLG\ncatanduni\nderivative233\n\nSpecial thanks to:\nBig_True')

def showMenu():
	startButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)
	optionsButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)
	helpButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)
	creditsButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)
	exitButton.pack(anchor='ne',side=tkinter.TOP,padx=50,pady=20,expand=True)

def hideMenu():
	startButton.pack_forget()
	optionsButton.pack_forget()
	helpButton.pack_forget()
	creditsButton.pack_forget()
	exitButton.pack_forget()

def showOptions():
	optionsBanner.pack(anchor='n',side=tkinter.TOP)
	volumeScale.pack(anchor='s',side=tkinter.TOP)
	volumeLabel.pack(anchor='s',side=tkinter.TOP)
	offsetScale.pack(anchor='s',side=tkinter.TOP)
	offsetLabel.pack(anchor='s',side=tkinter.TOP)

def hideOptions():
	optionsBanner.pack_forget()
	volumeScale.pack_forget()
	volumeLabel.pack_forget()
	offsetScale.pack_forget()
	offsetLabel.pack_forget()

def showHelp():
	helpBanner.pack(anchor='n',side=tkinter.TOP)
	helpContent.pack(anchor='n',side=tkinter.TOP)

def hideHelp():
	helpBanner.pack_forget()
	helpContent.pack_forget()

def showCredits():
	creditsBanner.pack(anchor='n',side=tkinter.TOP)
	creditsContent.pack(anchor='n',side=tkinter.TOP)

def hideCredits():
	creditsBanner.pack_forget()
	creditsContent.pack_forget()

def showBack():
	backButton.pack(anchor='ne',side=tkinter.BOTTOM,padx=50,pady=20)

def hideBack():
	backButton.pack_forget()

def hideAll():
	hideMenu()
	hideOptions()
	hideHelp()
	hideCredits()
	hideBack()

showMenu()
win.mainloop()