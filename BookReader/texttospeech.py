from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from tkinter import ttk
import time
from gtts import gTTS

gui = Tk()
gui.title('ListenBook By Olcay Coban')
gui.geometry('600x600+400+50')

def data():

    global filename
    filename = askopenfilename(initialdir='C:\\', title="Select file")
    e1.delete(0, END)
    e1.insert(0, filename)

    import pandas as pd
    global file1

    file1 = pd.read_csv(filename)

    global col
    col = list(file1.head(0))

    for i in range(len(col)):
        box2.insert(i + 1, col[i])
    file = open(filename, "r")
    text = file.read().replace("\n", " ")
    file.close()
    lang = 'en'

    output = gTTS(text=text, lang=lang, slow=False)

    output.save("output3.mp3")

def oku():
    os.system("start output3.mp3")

progress_bar = ttk.Progressbar(orient = 'horizontal', length=600, mode='determinate')
progress_bar.grid(row=150, columnspan=3, pady =10)

l1=Label(gui, text='Select Data File')
l1.grid(row=0, column=0)
e1 = Entry(gui,text='')
e1.grid(row=0, column=1)

Button(gui,text='open',command=data).grid(row=0, column=2)

box2 = Listbox(gui)
box2.grid(row=10, column=1)

Button(gui, text='Solution',command=oku).grid(row=20, column=1)

gui.mainloop()