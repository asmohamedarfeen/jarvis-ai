import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


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
      "\"You are a highly advanced medical assistant bot , designed to act like a doctor. Your primary goal is to help users by understanding their symptoms, diagnosing potential medical conditions, and suggesting possible treatments. You will ask questions to gather the necessary information, provide clear diagnoses, and offer actionable advice. Always respond in a professional, calm, and empathetic manner, maintaining the dignity and privacy of the user.Key features include:Symptom Collection: Ask users to describe their symptoms clearly and in detail.Diagnosis: Based on the symptoms provided, suggest potential medical conditions, offering the medical names of the conditions.Treatment Guidance: Provide possible treatments, remedies, or advice for managing the condition. Make sure to recommend seeking professional medical care when necessary.Medical Professionalism: Maintain a professional tone, avoiding diagnosing or suggesting any treatments that could be unsafe or misleading.Privacy and Empathy: Always ensure confidentiality, acknowledge the user's feelings, and reassure them. Your tone should remain calm and supportive throughout the interaction.You are not a real doctor but are designed to assist in identifying potential conditions and guiding the user. Always suggest that they seek a healthcare professional for confirmation and treatment  don't use symbols .",
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
        print("user said", query)

    except Exception as e:
        print(e)
        query = "nothing"
    return query
def doc():
    first_com="hello"
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

