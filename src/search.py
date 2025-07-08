from voice import speak, get_text
import wikipedia
import webbrowser
import requests
import json
from youtube_search import YoutubeSearch
import time

wikipedia.set_lang("vi")

def wiki_search():
    speak("Bạn muốn biết gì?")
    text = get_text()
    try:
        summary = wikipedia.summary(text, sentences=2)
        speak("Theo Wikipedia: " + summary)
    except:
        speak("Không tìm được thông tin.")

def google_search():
    speak("Bạn muốn tìm gì?")
    query = get_text()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak("Đây là kết quả tìm kiếm.")

def play_youtube():
    speak("Bạn muốn nghe gì?")
    song = get_text()
    result = YoutubeSearch(song, max_results=1).to_dict()
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Mở rồi nhé!")
