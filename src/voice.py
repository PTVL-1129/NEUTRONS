import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(text):
    print("Bot:", text)
    tts = gTTS(text=text, lang="vi")
    tts.save("temp.mp3")
    playsound.playsound("temp.mp3")
    os.remove("temp.mp3")

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Me:", end=" ")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            return r.recognize_google(audio, language="vi").lower()
        except:
            return ""

def get_text():
    while True:
        text = get_voice()
        if text:
            return text
