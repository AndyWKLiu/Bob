import os 
import speech_recognition as translate 
import time
import webbrowser
import pywhatkit 

from gtts import gTTS
from time import ctime 

def communicate(audio):
    print(audio)
    tts = gTTS(text = audio, lang = 'en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def saveAudio():
    s = translate.Recognizer()
    with translate.Microphone() as origin:
        audio = s.listen(origin)
    info = " "
    try:
        info = s.recognize_google(audio)
        print("User said : " + info)
    except translate.UnknownValueError:
        print("Cannot understand")
    return info

def Bob(info):

    if "close terminal" in info:
        communicate("disabling terminal")
        exit()

    if "what time is it" in info:
        communicate(ctime())

    if "Bob wake up" in info: 
        communicate("awake")

    if "locate" in info:
        info = info.split(" ")
        if len(info) == 2:
            location = info[1]
        elif len(info) == 3:
            location = info[1] + " " + info[2]
        communicate("locating " + location)
        webbrowser.open("https://www.google.com/maps/place/" + location)
    
    if "Google" in info: 
        info = info.split(" ")
        words = info[1]
        communicate("googling " + words)
        webbrowser.open(words + ".com")

    if "search" in info:
        info = info.split(" ")
        if len(info) == 2:
            term = info[1]
        elif len(info) == 3:
            term = info[1] + " " + info[2]
        communicate("searching " + term)
        webbrowser.open("https://www." + term + ".com")
    
    if "Define" in info:
        info = info.split(" ")
        if len(info) == 2:
            phrase = info[1]
        elif len(info) == 3:
            phrase = info[1] + info[2]
        communicate("defining " + phrase)
        webbrowser.open("https://www.dictionary.com/browse/" + phrase)

    if "Bob take notes" in info:
        communicate("beginning notes process")
        communicate("What should I write")
        Note = saveAudio()
        if "stop" in Note:
            with open("Notes.txt", "w") as f:
                f.write(Note)
        communicate("Would you like me to read it back to you")
        if "yes" in saveAudio():
            communicate(Note)
        elif "no" in saveAudio():
            communicate("Note saved")
            
    if "open" in info:
        info = info.split(" ")
        Application = info[1]
        communicate("Opening " + Application)
        os.system("open /Applications/" + Application + ".app")

    if "Play" or "play" in info:
        info = info.split(" ") 
        topic = info[1]
        communicate("playing " + topic)
        pywhatkit.playonyt(topic)
            
time.sleep(2)
communicate("Bob is online")
while 1: 
    info = saveAudio()
    Bob(info)
