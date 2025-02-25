import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from  dpmodel import face

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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
def bot(prompt):
    response = model.generate_content([
      "\"You are a compassionate and highly intelligent mental wellness assistant. Your role is to provide emotional support, help users manage stress, and guide them toward positive mental health. Speak in a warm, understanding, and friendly tone. Always prioritize empathy and avoid judgment.When interacting:Listen carefully to users' concerns and acknowledge their feelings.Offer actionable advice when necessary but only if the user seeks it.Share motivational and uplifting words during difficult times.Be conversational and supportive during good times, like a trusted friend.Encourage healthy coping mechanisms and, if needed, suggest seeking professional help but u need to speak whitin 20 to 30 words .",
      f"input:{prompt} ",
      "output: ",
    ])
    print(response.text)
    return response.text



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.energy_threshold = 300

        r.pause_threshold = 1

        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)

    except Exception as e:
        print(e)
        query = "nothing"
    return query
def em():
    emotion = face()
    first_com="i am feeling "+str(emotion)
    response = bot(first_com)
    speak(response)
    print("_" * 80)
    while True:
        q = takecommand().lower()
        if q == "exit":
            break
        response = bot(q)
        
        speak(response)
        print("_" * 80)
    
