# My personel asisstant

import speech_recognition as sr
import  pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Listening, please speak...")
    audio = r.listen(source)
try:
    command = r.recognize_google(audio, language="tr-TR")
    print("You said:    ", command)
    if "saat kaç" in command:
        from datetime import datetime
        now = datetime.now()
        speak(f"Şu an saat {now.hour} {now.minute}")
    elif "open the calculator" in command:
        speak("Calculator is opening.")
        import os
        os.system("calc")
    elif "google" in command:
        speak("Google açiliyor.")
        import webbrowser
        webbrowser.open("https://www.google.com")
    else:
        speak("Bu komutu anlayamadim.")

except sr.UnknownValueError:
    print("Ne dedigini anlayamadim.")
except sr.RequestError:
    print("Google hizmetine ulasilamadi.")