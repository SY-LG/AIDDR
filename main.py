from mttkinter import mtTkinter as tkinter
import json,time
from core import camera,chartLoader,music

infos={}
songNumber=0

# Buttons related functions

def startFunc():
	global infos
	with open('./data/infos.json','r') as File:
		infos=json.load(File)
	selectSong()

def selectSong():
	hideAll()
	showSelect()
	showBack()
	return 0

def prevFunc():
	global songNumber
	songNumber-=1
	hideSelect()
	showSelect()

def nextFunc():
	global songNumber
	songNumber+=1
	hideSelect()
	showSelect()

def confirmFunc():
	playMusic()

def playMusic():
	global infos,songNumber
	hideAll()
	win.update()
	time.sleep(0.5)
	cameraThread=camera.cameraThread()
	chartThread=chartLoader.chartLoaderThread(infos[songNumber]["chart"])
	musicThread=music.musicThread(path=infos[songNumber]["music"],volume=volumeScale.get())
	cameraThread.start()
	chartThread.start()
	musicThread.start()
	time.sleep(infos[songNumber]["time"]/1000)
	cameraThread.quit=True
	chartThread.quit=True
	musicThread.quit=True
	time.sleep(1)
	cameraThread.join()
	chartThread.join()
	musicThread.join()
	showResults(None)

def showResults(results):
	showMenu()

def optionsFunc():
	hideAll()
	showOptions()
	showBack()

def helpFunc():
	hideAll()
	showHelp()
	showBack()

def creditsFunc():
	hideAll()
	showCredits()
	showBack()

def backFunc():
	hideAll()
	showMenu()

# tkinter objects

win=tkinter.Tk()
win.title('AIDDR')
win.geometry('1400x800')

startButton=tkinter.Button(win,command=startFunc,text='Start')
optionsButton=tkinter.Button(win,command=optionsFunc,text='Options')
helpButton=tkinter.Button(win,command=helpFunc,text='Help')
creditsButton=tkinter.Button(win,command=creditsFunc,text='Credits')
exitButton=tkinter.Button(win,command=lambda : win.destroy(),text='Exit')

backButton=tkinter.Button(win,command=backFunc,text='Back')

selectBanner=tkinter.Label(win,text='Select music',font=('Arial', 15))
selectLabel=tkinter.Label(win,pady=20)
prevButton=tkinter.Button(win,command=prevFunc,text='Prev')
nextButton=tkinter.Button(win,command=nextFunc,text='Next')
confirmButton=tkinter.Button(win,command=confirmFunc,text='Comfirm')

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

# hide and show functions

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

def showSelect():
	global infos,songNumber
	selectLabel['text']=f'name:{infos[songNumber]["name"]}'
	selectBanner.pack(anchor='n',side=tkinter.TOP)
	selectLabel.pack(anchor='s',side=tkinter.BOTTOM)
	prevButton.place(relx=0.7,rely=0.2)
	nextButton.place(relx=0.7,rely=0.3)
	confirmButton.place(relx=0.7,rely=0.4)
	if songNumber==0:
		prevButton.place_forget()
	elif songNumber==len(infos)-1:
		nextButton.place_forget()

def hideSelect():
	selectBanner.pack_forget()
	selectLabel.pack_forget()
	prevButton.place_forget()
	nextButton.place_forget()
	confirmButton.place_forget()

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
	hideSelect()
	hideOptions()
	hideHelp()
	hideCredits()
	hideBack()

showMenu()
win.mainloop()