import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from tkinter import *

freq=44100
duration=5

def record():
    print("Startingggg!!!!")
    record=sd.rec(int(duration*freq), samplerate=freq,channels=2)

    sd.wait()
    write('recorddata0.wav',freq,record)
    wv.write('recording1.wav',record,freq,sampwidth=2)
    print("Finished!!!")

root = Tk()
root.title('Record Audio')
root.geometry('300x200+100+50')

buton=Button(root)
buton.config(text="Record it!!!")
buton.config(command=record)
buton.pack()

root.mainloop()