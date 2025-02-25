import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
#import playsound
from googletrans import Translator
import googletrans 
from gtts import gTTS
from fnmatch import translate
import googletrans
from time import sleep
import pyautogui
import pywhatkit
from pynput.keyboard import Key,Controller
import pyfirmata

#board=pyfirmata.Arduino("COM5")
#board.digital[2].write(1)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing,sir")
    if "tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("tabs closed sir")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed sir")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed sir")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed sir")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed sir")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

def searchYoutube(query):
        speak("This is what I found for your search!")
        query = query.replace("search in youtube","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


def searchGoogle(query):
    import wikipedia as googleScrap
    query = query.replace("jarvis","")
    query = query.replace("google search","")
    query = query.replace("google","")
    speak("This is what I found on google")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak(result)

    except:
        speak("No speakable output available")

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning BOSS!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon boss!")   

    else:
        speak("Good Evening boss!")



def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1

        audio=r.listen(source)
  
    try:   
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
        
    except Exception as e:
        print(e)
        query="nothing"
    return query


def jarvis():
    
    
    wishMe()
    
    while True:
        g="w"

        if 'w' in g:
            speak("i am on,,,what can i do for you sir")
            


            
            
            while True:
                query = input("enter here:")
                
                if "about you" in query:
                    speak("i was a  virtual assistant,named as jarvis and   i  was created by arfeen")
                    
                #code for playing games
                elif "play a game" in query:
                    from gametext import game_play
                    game_play()
                #code for headline
                elif "news" in query:
                    from NewsReadtext import latestnews
                    latestnews()

                #for recognation of face
                elif 'open your eyes' in query:
                    from main_video import face
                    face()
                #schedule mu day
                elif "schedule my day" in query:
            
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takecommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()


                #code for chat
                elif "thank you jarvis" == query:
                    speak("welcome sir")
                elif "hi jarvis" == query:
                    speak("hi,sir")


                elif "how are you" == query:
                    speak("i am fine sir,what about you sir?")

                elif "bye" == query:
                    speak("bye")
                elif "what is your name" == query:
                    speak( "my name is jarvis sir ")
                
                elif "in tamil" in query:
                    from testing import say_tk
                    say_tk()
                    

                #code for screenshot
                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                #code for open app
                elif "open" in query:
                    openappweb(query)
                    
                #code for close app
                elif "close" in query:
                    closeappweb(query)
                    
                #code for search in youtube
                elif "youtube" in query:
                    searchYoutube(query)
                #code for send massage in whatsapp
                elif "whatsapp" in query:
                    from Whatsapptext import sendMessage
                    sendMessage()
                    
                #code for control youtube video
                elif "stop" in query:
                    pyautogui.press("k")
                    speak("video paused sir")
                
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played sir")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted sir")
                elif "volume up" in query:
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    speak("Turning volume down, sir")
                    volumedown()
                #code to search in wikipedia
                elif 'wikipedia' in query:
                    speak('Searching in Wikipedia sir...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                #code for time
                elif 'the time' in query:
                    time=datetime.datetime.now().strftime("%H:%M")
                    speak(time)
                #code for exit from while loop
                elif 'quiet' in query:
                    speak("quitting sir")
                    break
                elif 'light' in query:
                    speak("turning on light sir")
                    board.digital[2].write(0)

                elif 'light  off' in query:
                    speak("turning off light sir")
                    board.digital[2].write(1)
                #code for stop the file
                elif "exit" in query:
                    exit()
                #code for else case
                else:
                    #code for case1 in this case no input for user
                    if "nothing" == query:
                        speak("say something sir")
                    #code for search google
                    else:
                        speak(query+"searching om google sir")
                        searchGoogle(query)


jarvis()
                   