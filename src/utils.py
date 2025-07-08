from voice import speak
import datetime
import random

AI_sorry = ["Tôi không hiểu", "Nói to lên", "Không nghe rõ"]
AI_suggest = ["Tôi có thể giúp gì cho bạn?", "Cần tôi làm gì?"]

def timenow(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút")
    elif "ngày" in text:
        speak(f"Hôm nay là ngày {now.day} tháng {now.month}, năm {now.year}")
    else:
        speak(random.choice(AI_sorry))

def stop():
    speak("Tạm dừng hệ thống.")

def end():
    speak("Tạm biệt! Hẹn gặp lại.")
    exit()

def random_response(type):
    if type == "suggest":
        return random.choice(AI_suggest)
    return "..."
