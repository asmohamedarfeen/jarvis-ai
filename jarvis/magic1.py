from time import sleep
import random
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def magic():
    
    speak("ok imagine a number in you mind first")
    sleep(0.9)
    speak("now multiply the number with 2")
    a=[2,4,6,8,10,12,14,16,18,20]
    add=random.choice(a)
    n=str(add)
    com="add number "+n+"  with result"
    sleep(0.7)
    speak(com)
    sleep(0.7)
    speak("now divide it by 2")
    sleep(0.7)
    speak("subtract the number which you   imagine first with result ")
    result=add//2
    n1=str(result)

    com1="now there is a number in you mind and that is "+n1
    sleep(0.7)
    speak(com1)

