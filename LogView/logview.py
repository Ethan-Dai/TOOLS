#!/usr/bin/python3 
from tkinter import *
from tkinter.ttk import *
from linecache import *
import os


# main window
win = Tk()
win.wait_visibility(win)
#win.wm_attributes('-topmost',1)
win.attributes("-alpha",1.0)
win.title("LogView")
win.geometry('600x800')

# data source
command = StringVar()
data_comb = Combobox(win, textvariable=command, values=['dmesg','ls'])
data_comb.current(0)
data_comb.place(x=0,y=0,height=30,width=200)

# filter
filt = StringVar()
filt_comb = Combobox(win, textvariable=filt, values=['Last 10 lines','Last 20 lines','After booting'])
filt_comb.current(0)
filt_comb.place(x=220,y=0,height=30,width=120)


# Text box		
def update():
	text.delete(1.0,END)
	process = os.popen(command.get()) # return file
	lines = process.readlines()
	process.close()
	win.title(command.get())
	if filt.get()=="Last 10 lines":
		for line in lines[-10::]:
    			text.insert(END,line)
	elif filt.get()=="Last 20 lines":
                for line in lines[-20::]:
                        text.insert(END,line)
	elif filt.get()=="After booting":
		for line in lines:
			text.insert(END,line)
	else:
		for line in lines:
			if line.find(filt.get())>0:
				text.insert(END,line)
	text.insert(END,"----------------------END----------------------\n\n")
	if(auto_fresh.get()):
		win.after(1000,update)

text = Text(win,font=('Open Sans',12))
text.place(x=0,y=30,relwidth=1.0,relheight=1.0)

sl = Scrollbar(text)
sl.pack(side = RIGHT,fill = Y)
sl['command'] = text.yview


# fresh the data
fresh_bton = Button(win, text='↻', command = update)
fresh_bton.place(x=350,y=0,height=30,width=30)
auto_fresh = IntVar()
fresh_check = Checkbutton(win,text='Auto',variable=auto_fresh)
fresh_check.place(x=390,y=0,height=30,width=60)

mainloop()
