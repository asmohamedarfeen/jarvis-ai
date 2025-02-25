import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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


def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9ffed7ad9bdf46028257df7549ceba4a",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9ffed7ad9bdf46028257df7549ceba4a",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9ffed7ad9bdf46028257df7549ceba4a",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9ffed7ad9bdf46028257df7549ceba4a",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9ffed7ad9bdf46028257df7549ceba4a",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9ffed7ad9bdf46028257df7549ceba4a"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    query=input("enter here:")
    field = query
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        speak("do you more news say yes or you want to stop say no")
        query=input("enter here:")
        a =query
        if "yes" in a:
            pass
        elif "no" in a:
            break
        
    speak("thats all")
