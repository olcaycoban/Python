from gtts import gTTS
import os

file=open("deneme.txt","r")
text=file.read().replace("\n"," ")
file.close()
lang='en'

output=gTTS(text=text,lang=lang,slow=False)

output.save("output2.mp3")
os.system("start output2.mp3")