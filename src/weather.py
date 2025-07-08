import requests
from voice import speak, get_text
import datetime

def check_weather():
    speak("Bạn muốn xem thời tiết ở đâu?")
    city = get_text()
    api_key = "API_KEY_CỦA_MÀY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()

    if res.get("cod") != 200:
        speak("Không tìm thấy thông tin.")
        return

    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    speak(f"Nhiệt độ ở {city} là {temp} độ. Trời {desc}")
