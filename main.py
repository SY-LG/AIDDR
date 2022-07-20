from mttkinter import mtTkinter as tkinter
from PIL import Image,ImageTk
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
	startTime=time.perf_counter()+1
	cameraThread=camera.cameraThread(path=infos[songNumber]["chart"],startTime=startTime)
	chartThread=chartLoader.chartLoaderThread(path=infos[songNumber]["chart"],startTime=startTime,offset=offsetNoteScale.get())
	musicThread=music.musicThread(path=infos[songNumber]["music"],startTime=startTime,volume=volumeScale.get(),offset=offsetMusicScale.get())
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
	showResults({"Score":114514,"total":4,"Perfect":2,"Good":1,"Bad":0,"Miss":1})
	showBack()

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
selectCanvas=tkinter.Canvas(win,height=500,width=500)
selectLabel=tkinter.Label(win,pady=20)
prevButton=tkinter.Button(win,command=prevFunc,text='Prev')
nextButton=tkinter.Button(win,command=nextFunc,text='Next')
confirmButton=tkinter.Button(win,command=confirmFunc,text='Comfirm')

resultsBanner=tkinter.Label(win,text='Results',font=('Arial',15))
resultsLabel=tkinter.Label(win,pady=20)

optionsBanner=tkinter.Label(win,text='Options',font=('Arial', 15))

volumeScale=tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL)
volumeScale.set(100)
volumeLabel=tkinter.Label(win,text='volume')

offsetNoteScale=tkinter.Scale(win,from_=-500,to=500,orient=tkinter.HORIZONTAL)
offsetNoteScale.set(0)
offsetNoteLabel=tkinter.Label(win,text='offset of notes')

offsetMusicScale=tkinter.Scale(win,from_=-500,to=500,orient=tkinter.HORIZONTAL)
offsetMusicScale.set(0)
offsetMusicLabel=tkinter.Label(win,text='offset of music')

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
	showSelect.img=ImageTk.PhotoImage(Image.open(infos[songNumber]["illustration"]).resize((500,500)))
	selectCanvas.create_image(250,250,image=showSelect.img)
	selectLabel['text']=f'''name:{infos[songNumber]["name"]}
	{songNumber+1}/{len(infos)}
	'''
	selectBanner.pack(anchor='n',side=tkinter.TOP)
	selectCanvas.pack(anchor='s',side=tkinter.TOP)
	selectLabel.pack(anchor='s',side=tkinter.TOP)
	prevButton.place(relx=0.7,rely=0.2)
	nextButton.place(relx=0.7,rely=0.3)
	confirmButton.place(relx=0.7,rely=0.4)
	if songNumber==0:
		prevButton.place_forget()
	elif songNumber==len(infos)-1:
		nextButton.place_forget()

def hideSelect():
	selectBanner.pack_forget()
	selectCanvas.pack_forget()
	selectLabel.pack_forget()
	prevButton.place_forget()
	nextButton.place_forget()
	confirmButton.place_forget()

def showResults(results):
	resultsLabel['text']=f'''Score:{results['Score']}
	Perfect:{results['Perfect']}
	Good:{results['Good']}
	Bad:{results['Bad']}
	Miss:{results['Miss']}
	'''
	resultsBanner.pack(anchor='n',side=tkinter.TOP)
	resultsLabel.pack(anchor='s',side=tkinter.BOTTOM)

def hideResults():
	resultsBanner.pack_forget()
	resultsLabel.pack_forget()

def showOptions():
	optionsBanner.pack(anchor='n',side=tkinter.TOP)
	volumeScale.pack(anchor='s',side=tkinter.TOP)
	volumeLabel.pack(anchor='s',side=tkinter.TOP)
	offsetNoteScale.pack(anchor='s',side=tkinter.TOP)
	offsetNoteLabel.pack(anchor='s',side=tkinter.TOP)
	offsetMusicScale.pack(anchor='s',side=tkinter.TOP)
	offsetMusicLabel.pack(anchor='s',side=tkinter.TOP)

def hideOptions():
	optionsBanner.pack_forget()
	volumeScale.pack_forget()
	volumeLabel.pack_forget()
	offsetNoteScale.pack_forget()
	offsetNoteLabel.pack_forget()
	offsetMusicScale.pack_forget()
	offsetMusicLabel.pack_forget()

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
	hideResults()
	hideOptions()
	hideHelp()
	hideCredits()
	hideBack()

showMenu()
win.mainloop()