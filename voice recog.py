import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizer...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
# sptext()
            
def txspeech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)          #voices[0] means male voice [1] means female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()
    
# txspeech("Hello superstar king Awanish ")

if __name__=='__main__':
    data1 = sptext().lower()
    if "your name" in data1:
        name = "my name is awanish singh"
        txspeech(name)
    elif "time" in data1:
        time = datetime.datetime.now().strftime("%I%M%p")
        txspeech(time)
    elif 'youtube' in data1:
        webbrowser.open("https://www.youtube.com/")
    
    elif 'joke' in data1:
        joke_1 = pyjokes.get_joke(language="en",category="neutral")
        print(joke_1)
        txspeech(joke_1)
        
    