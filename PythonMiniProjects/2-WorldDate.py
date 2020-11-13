from datetime import datetime
import pytz
from tkinter import *

def get_value():
    zone=giris.get()
    country=giris2.get()
    country_time_zone = pytz.timezone(zone+'/'+country)
    country_time = datetime.now(country_time_zone)
    yazi.config(text=country)
    yazi2.config(text=country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))

root = Tk()
root.title('how to get text from textbox')
root.geometry('300x200+100+50')

giris=Entry(root)
giris.pack()
giris2=Entry(root)
giris2.pack()

buton=Button(root)
buton.config(text="What time is it ?")
buton.config(command=get_value)
buton.pack()

yazi=Label(root)
yazi.config(text="İl")
yazi.pack()

yazi2=Label(root)
yazi2.config(text="İl")
yazi2.pack()


giris.mainloop()