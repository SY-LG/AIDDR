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
	startTime=time.perf_counter()+3
	cameraThread=camera.cameraThread(path=infos[songNumber]["chart"],startTime=startTime)
	chartThread=chartLoader.chartLoaderThread(path=infos[songNumber]["chart"],startTime=startTime,offset=offsetNoteScale.get())
	musicThread=music.musicThread(path=infos[songNumber]["music"],startTime=startTime,volume=volumeScale.get(),offset=offsetMusicScale.get())
	cameraThread.start()
	chartThread.start()
	musicThread.start()
	time.sleep(3+infos[songNumber]["time"]/1000)
	cameraThread.quit=True
	chartThread.quit=True
	musicThread.quit=True
	time.sleep(1)
	cameraThread.join()
	chartThread.join()
	musicThread.join()
	showResults(cameraThread.finalResult)
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
	start_window.create_image(590,354, image=credits_photo)
	hideAll()
	showCredits()
	showBack()

def backFunc():
	hideAll()
	showMenu()

# tkinter objects



win=tkinter.Tk()
win.title('AIDDR')

#images
start_photo_path = "./data/pictures/start.png"
credits_photo_path = "./data/pictures/credits.png"
help_photo_path = "./data/pictures/help.png"
select_photo_path = "./data/pictures/option.png"

start_img = Image.open(start_photo_path)
credits_img = Image.open(credits_photo_path)
options_img = Image.open(credits_photo_path)
help_img = Image.open(help_photo_path)
select_img = Image.open(select_photo_path)

global start_photo,credits_photo,options_photo,help_photo
start_photo = ImageTk.PhotoImage(start_img)
credits_photo = ImageTk.PhotoImage(credits_img)
options_photo = ImageTk.PhotoImage(options_img)
help_photo = ImageTk.PhotoImage(help_img) 
select_photo = ImageTk.PhotoImage(select_img) 

#开始窗口
start_window = tkinter.Canvas(win, width=1180,height=708)
start_window.create_image(590,354, image=start_photo)
start_window.pack()
 

#开始界面五个按钮
button_photo = tkinter.PhotoImage(file="./data/pictures/back.png")

startButton=tkinter.Button(win,command=startFunc,text='Start',fg="white",image=button_photo,compound = tkinter.CENTER)
optionsButton=tkinter.Button(win,command=optionsFunc,text='Options',fg="white",image=button_photo,compound = tkinter.CENTER)
helpButton=tkinter.Button(win,command=helpFunc,text='Help',fg="white",image=button_photo,compound = tkinter.CENTER)
creditsButton=tkinter.Button(win,command=creditsFunc,text='Credits',fg="white",image=button_photo,compound = tkinter.CENTER)
exitButton=tkinter.Button(win,command=lambda : win.destroy(),text='Exit',fg="white",image=button_photo,compound = tkinter.CENTER)

#退出
backButton=tkinter.Button(win,command=backFunc,text='Back',fg="white",bg="#40E0D0")

#选择界面
selectBanner=tkinter.Label(win,text='Select music',font=('Arial', 12),fg="white",bg="#40E0D0")
selectCanvas=tkinter.Canvas(win,height=500,width=500)
selectLabel=tkinter.Label(win,fg='cyan')
prevButton=tkinter.Button(win,command=prevFunc,text='Prev',fg="white",bg="#40E0D0")
nextButton=tkinter.Button(win,command=nextFunc,text='Next',fg="white",bg="#40E0D0")
confirmButton=tkinter.Button(win,command=confirmFunc,text='Comfirm',fg="white",bg="#40E0D0")



resultsBanner=tkinter.Label(win,text='Results',font=('Arial',15))
resultsLabel=tkinter.Label(win,pady=20)

#选择界面
optionsBanner=tkinter.Label(win,text='Options',font=('Arial', 15),fg="blue",bg="whitesmoke")

volumeScale=tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,fg="blue")
volumeScale.set(100)
volumeLabel=tkinter.Label(win,text='volume',fg="blue")

offsetNoteScale=tkinter.Scale(win,from_=-2000,to=2000,orient=tkinter.HORIZONTAL,fg="blue")
offsetNoteScale.set(0)
offsetNoteLabel=tkinter.Label(win,text='offset of notes',fg="blue")

offsetMusicScale=tkinter.Scale(win,from_=-2000,to=2000,orient=tkinter.HORIZONTAL,fg="blue")
offsetMusicScale.set(0)
offsetMusicLabel=tkinter.Label(win,text='offset of music',fg="blue")

#帮助界面
helpBanner=tkinter.Label(win,text='Help of AIDDR',font=('Arial', 15),fg="cyan")
helpContent=tkinter.Label(win,text='''
	What is AIDDR?\n
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
	'''
	,fg="cyan",font=('Arial', 7))

#感谢界面
creditsBanner=tkinter.Label(win,text='AIDDR\n@AI001-AIDDR team 2022',font=('Arial', 10),fg="cyan")
creditsContent=tkinter.Label(win,text='Team members:\nSYLG\ncatanduni\nderivative233\n\nSpecial thanks to:\nBig_True',fg="cyan")

# hide and show functions


def showMenu():
	startButton.place(x=722,y=180,height=70,width=130)
	optionsButton.place(x=722,y=330,height=70,width=130)
	helpButton.place(x=0,y=0,height=50,width=50)
	creditsButton.place(x=0,y=60,height=50,width=50)
	exitButton.place(x=722,y=480,height=70,width=130)

def hideMenu():
	startButton.place_forget()
	optionsButton.place_forget()
	helpButton.place_forget()
	creditsButton.place_forget()
	exitButton.place_forget()

	#start后具体的选择界面
def showSelect():
	start_window.create_image(590,354, image=select_photo)

	global infos,songNumber
	showSelect.img=ImageTk.PhotoImage(Image.open(infos[songNumber]["illustration"]).resize((500,500)))
	start_window.create_image(630,350,image=showSelect.img)
	selectLabel['text']=f'name:{infos[songNumber]["name"]}\n{songNumber+1}/{len(infos)}'
	selectBanner.place(x=570,y=30,height=50,width=150)
	selectLabel.place(x=570,y=650,height=50,width=150)
	prevButton.place(x=0.8*1180,y=0.3*708)
	nextButton.place(x=0.8*1180,y=0.5*708)
	confirmButton.place(x=0.8*1180,y=0.7*708)
	if songNumber==0:
		prevButton.place_forget()
	elif songNumber==len(infos)-1:
		nextButton.place_forget()

def hideSelect():
	start_window.create_image(590,354, image=start_photo)
	selectBanner.place_forget()
	selectCanvas.place_forget()
	selectLabel.place_forget()
	prevButton.place_forget()
	nextButton.place_forget()
	confirmButton.place_forget()
	#结果界面
def showResults(results):
	resultsLabel['text']=f'''
	Score:{results['Score']}
	Perfect:{results['Perfect']}
	Good:{results['Good']}
	Bad:{results['Bad']}
	Miss:{results['Miss']}
	'''
	resultsBanner.place(x=570,y=30,height=50,width=150)
	resultsLabel.place(x=570,y=200,height=200,width=150)

def hideResults():
	resultsBanner.place_forget()
	resultsLabel.place_forget()
	#选择界面
def showOptions():
	start_window.create_image(590,354, image=options_photo)
	optionsBanner.place(x=510,y=160,height=50,width=200)
	volumeScale.place(x=510,y=210,height=50,width=200)
	volumeLabel.place(x=510,y=260,height=50,width=200)
	offsetNoteScale.place(x=510,y=310,height=50,width=200)
	offsetNoteLabel.place(x=510,y=360,height=50,width=200)
	offsetMusicScale.place(x=510,y=410,height=50,width=200)
	offsetMusicLabel.place(x=510,y=460,height=50,width=200)

def hideOptions():
	start_window.create_image(590,354, image=start_photo)
	optionsBanner.place_forget()
	volumeScale.place_forget()
	volumeLabel.place_forget()
	offsetNoteScale.place_forget()
	offsetNoteLabel.place_forget()
	offsetMusicScale.place_forget()
	offsetMusicLabel.place_forget()
	#帮助界面
def showHelp():
	start_window.create_image(590,354, image=help_photo)
	helpBanner.place(x=840,y=100,height=50,width=150)
	helpContent.place(x=705,y=150,height=400,width=400)

def hideHelp():
	start_window.create_image(590,354, image=start_photo)
	helpBanner.place_forget()
	helpContent.place_forget()
	#感谢界面
def showCredits():
	start_window.create_image(590,354, image=credits_photo)
	creditsBanner.place(x=510,y=210,height=50,width=200)
	creditsContent.place(x=510,y=260,height=200,width=200)

def hideCredits():
	start_window.create_image(590,354, image=start_photo)
	creditsBanner.place_forget()
	creditsContent.place_forget()
	#返回按钮
def showBack():
	backButton.place(x=1000,y=650,height=50,width=100)

def hideBack():
	backButton.place_forget()

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
