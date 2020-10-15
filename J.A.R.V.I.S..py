import pyttsx3  ### pip install pyttsx3 
import datetime
import speech_recognition as sr #### pip install speech_Recognition
import wikipedia### install wikipedia
import webbrowser


engine = pyttsx3.init('sapi5') ### Speech API 

voices = engine.getProperty('voices')### details of current voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()## without this command speech will not be audible
  
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")  

    speak("I am jarvis sir.Please tell me how may I help you")  

def takeCommand(): ## takes microphone input from the user and returns string input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
         print("Recognizing...")
         query = r.recognize_google(audio, language = 'en-in')
         print(f"User said: {query}\n")

    except Exception:
        ### print(e)
            print("say that again please...")
            return "None" 
    return query           

if __name__ == "__main__":   
    wishme()
    while True:
        query=takeCommand().lower()   
#### logic for executing task
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("google.com")    
if 'quit' in query:
    exit()  