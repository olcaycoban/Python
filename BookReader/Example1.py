from gtts import gTTS
import os

text="Merhana nasılsın ?"

lang='tr'

output=gTTS(text=text,lang=lang,slow=False)
output.save('output1.mp3')
os.system('start output1.mp3')