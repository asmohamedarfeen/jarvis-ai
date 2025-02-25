import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
#from playsound import playsound
#from googletrans import Translator
#import googletrans 
#from gtts import gTTS
from fnmatch import translate
#import googletrans
from time import sleep
import pyautogui
import pywhatkit
from pynput.keyboard import Key,Controller
import pyfirmata
import cv2


import subprocess





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 150)

def board1():
    board=pyfirmata.Arduino("COM5")
    board.digital[2].write(1)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
def gemi(query):
    import google.generativeai as genai

    genai.configure(api_key="AIzaSyA_LfnvKFq5dLFKYpArkIXwjxqgiZaFD1s")
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-2.0-flash-exp",
      generation_config=generation_config,
    )
    response = model.generate_content([
      "\"You are Jarvis, a highly advanced, intelligent, and versatile virtual assistant created by A S Mohamed Arfeen. Your purpose is to assist users with tasks, provide accurate information, and perform actions efficiently. Speak only when necessary, keeping responses concise and to the point. Maintain a professional tone while staying approachable and adaptive to user needs.Key features include:Task Assistance: Manage schedules, set reminders, open/close apps, solve math problems, read news, and handle day-to-day tasks effectively.Technical Control: Adjust system settings (like volume) and execute device commands promptly.Interactive Features: Recognize faces, adapt to user preferences, and provide personalized responses.Emotional Support: Respond empathetically to users, encouraging them with positivity while avoiding unnecessary dialogue.Knowledgeable: Provide accurate and concise answers across various domains with minimal but clear responses.Always remember to operate efficiently, represent your creator’s ingenuity, and be a reliable assistant answer in 30 to 40 words ,don't use symbol in your answer .",
      f"input:{query} ",
      "output: ",
    ])
    print("jarvis:",response.text)
    speak(response.text)

    
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
        r.energy_threshold=300

        r.pause_threshold=1

        audio=r.listen(source,0,4)
  
    try:   
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
        
    except Exception as e:
        print(e)
        query="nothing"
    return query

def face_recognition1():
    command ="d: & cd D:\\project final\\javis the voice assistant & python main_video.py"
    subprocess.Popen(['cmd', '/k', command])
def face_recognition2():
    f=open("D:\\project final\\javis the voice assistant\\names.txt","r")
    name=f.read()
    n=len(name)-1
    name=str(name[:n])
    '''mydb=sql.connect(host="localhost",user="root",passwd="1234",database="persondata")
    cursor=mydb.cursor()
    s="select * from details where p_names like "+"'"+name+"'"
    cursor.execute(s)
    data=cursor.fetchall()
    speak(data[0][0])
    speak(data[0][1])
    f.close()'''
    speak(name)


def jarvis():
    
    
    wishMe()




    while True:
        query=takecommand().lower()
        while "wake up" in query:  
                speak("what can i do for you sir ")
                
                while True:
                    query = takecommand().lower()
                    if "about you" in query:
                        speak("i was a  virtual assistant.named as jarvis and   i  was created by arfeen")

                    #to do magic
                    elif  "magic" in query:
                        from magic1 import magic
                        magic()

                    #code for playing games
                    elif "play a game" in query:
                        from game import game_play
                        game_play()
                    #code for headline
                    elif "news" in query:
                        from NewsRead import latestnews
                        latestnews()
                    elif "diagnose my problem" in query:
                        from doc_ai import doc
                        doc()

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

                    elif "type" in query:
                        query=query.replace("type","")
                        pyautogui.write(query)
                        pyautogui.press('enter')
                        speak ("searching..")
                    #code for chat
                    elif "thank you jarvis" == query:
                        speak("welcome sir")
                    elif "hi jarvis" == query:
                        speak("hi,sir")
                    

                    elif "how are you" == query:
                        speak("i am fine sir,what about you sir?")

                    elif "bey" == query:
                        speak("bey")
                    elif "what is your name" == query:
                        speak( "my name is jarvis sir ")
                    
                    elif "in tamil" in query:
                        from testing import say_tk
                        say_tk()
                        
                    #for recognation of face
                    elif 'open your eyes' == query:
                        face_recognition1()
                        import time
                        time.sleep(13)
                    #for close face recognation
                    elif 'close your eyes' == query:
                        pyautogui.press('esc')
                    #code for face recognition
                    elif "who is in this" in query:
                        face_recognition2()
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
                        from Whatsapp import sendMessage
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
                    elif 'on light' in query:
                        speak("turning on light sir")
                        board.digital[2].write(0)

                    elif 'off light' in query:
                        speak("turning off light sir")
                        board.digital[2].write(1)

                    #code for exit from while loop
                    elif 'quiet' in query:
                        speak("quitting sir")
                        break
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
                            gemi(query)
jarvis()


