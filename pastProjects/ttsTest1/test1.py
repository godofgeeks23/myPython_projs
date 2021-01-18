# using the gtts module
from gtts import gTTS
import os
from playsound import playsound
mytext = 'This is a Sample Text To Speech Test'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
playsound('welcome.mp3')
