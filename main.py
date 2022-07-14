import tkinter

def start():
	txt=tkinter.Label(win,text='Start')
	txt.pack(anchor='nw',side=tkinter.LEFT,padx=50,pady=20)

def option():
	showOption()

def volumeSet(value):
	global settings
	settings['volume']=value

def offsetSet(value):
	global settings
	settings['offset']=value

settings={'volume':100,'offset':0}

win=tkinter.Tk()
win.title('AIDDR')
win.geometry('800x800')

startButton=tkinter.Button(win,command=start,text='Start')
optionButton=tkinter.Button(win,command=option,text='Option')
exitButton=tkinter.Button(win,command=lambda : win.destroy(),text='Exit')

volumeScale=tkinter.Scale(win,from_=0,to=100,command=volumeSet,orient=tkinter.HORIZONTAL)
volumeLabel=tkinter.Label(win,text='volume')

offsetScale=tkinter.Scale(win,from_=-100,to=100,command=offsetSet,orient=tkinter.HORIZONTAL)
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
	offsetScale.pack_forget()
	offsetLabel.pack_forget()

def hideAll():
	hideMenu()
	hideOption()

showMenu()
win.mainloop()