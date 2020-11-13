from datetime import datetime
import pytz
from tkinter import *

root = Tk()
root.title('how to get text from textbox')
root.geometry('500x400+100+50')

Lb1 = Listbox(root)

count=1
for i in pytz.all_timezones:
    Lb1.insert(count,i)
    count=count+1

Lb1.pack()

yazi2=Label(root)
yazi2.config(text="Clock")
yazi2.pack()

def get_clock():
    cs=Lb1.get(100)
    yazi2.config(text=str(cs))
    yazi2.pack()

buton=Button(root)
buton.config(text="What time is it ?")
buton.config(command=get_clock())
buton.pack()

yazi=Label(root)
yazi.config(text="Timezone-Country")
yazi.pack()

root.mainloop()

"""
    country_time_zone = pytz.timezone(strzone_country)
    country_time = datetime.now(country_time_zone)
    yazi.config(text=zone_country)
    yazi2.config(text=country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
"""