# using the pyttsx3 module
import pyttsx3
engine = pyttsx3.init()
engine.say("This is my default voice")
engine.runAndWait()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
engine.say("This is my slower voice")
engine.runAndWait()

"""VOLUME"""
volume = engine.getProperty(
    'volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 2.0)    # setting up volume level  between 0 and 1
engine.say("This is my voice at louder volume")
engine.runAndWait()

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)
engine.say("This is my voice version 0")
engine.runAndWait()
print(voices)
