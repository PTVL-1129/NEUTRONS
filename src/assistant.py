from voice import get_text, speak
from system_info import system_info
from weather import check_weather
from dictionary import check_dictionary
from search import wiki_search, google_search, play_youtube
from utils import timenow, stop, end, random_response
import time

def call_jarvis():
    speak(random_response("suggest"))
    while True:
        text = get_text()
        if not text:
            continue

        if any(i in text for i in ["tạm biệt", "dừng", "hẹn gặp"]):
            end()
        elif "giúp gì" in text or "giúp đỡ" in text:
            # gọi chức năng help nếu muốn
            pass
        elif "giới thiệu" in text or "bạn là ai" in text:
            system_info()
        elif "tra từ điển" in text:
            check_dictionary()
        elif "thời tiết" in text:
            check_weather()
        elif "mấy giờ" in text or "ngày bao nhiêu" in text:
            timenow(text)
        elif "youtube" in text or "nhạc" in text:
            play_youtube()
        elif "định nghĩa" in text:
            wiki_search()
        elif "google" in text or "tra cứu" in text:
            google_search()
        else:
            wiki_search()

def call_infor():
    speak("Xin chào! Tôi là NEUTRONS.")
    name = input("Bạn tên gì? ")
    speak(f"Rất vui được gặp bạn, {name}")
