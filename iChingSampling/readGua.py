# this function will read the text file for each 'gua'
# line by line 

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[25].id)

def readYao(yao):
    engine.say(yao)
    engine.runAndWait()