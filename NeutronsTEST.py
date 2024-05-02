import irregular
import os
import playsound
import speech_recognition as sr
import time
import cv2
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import random
import requests
import urllib
import urllib.request as urllib2
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from docx import Document
from setuptools import setup
from Cython.Build import cythonize
from pathlib import Path
import numpy as np
import math

language = 'vi'
path = ChromeDriverManager().install()
wikipedia.set_lang('vi')\

AI_ads =("""
            Xin chào đây là NEUTRONS - một Trợ lý ảo tiếng Việt đến từ đội ngũ lớp 9G trường Trung học Cơ sở Lê Hồng Phong. 
            Tôi được tạo ra từ hàng trăm dòng code từ những người lập trình viên tuyệt vời nhất của lớp 9G.
            Tôi rất mong mọi người sẽ ủng hộ tôi!
        """,
        """
            Xin chào đây là NEUTRONS - một Trợ lý ảo tiếng Việt đến từ lớp 9G.
            Tôi mới là phiên bản BETA 1.0.
            Mong mọi người góp ý và hỗ trợ tôi hoàn thiện bản thân ạ!
        """,
        """
            Xin chào tôi là NEUTRONS - Đến từ lớp 9G.
            Tuy có cuộc sống ảo trong máy tính nhưng tôi rất yêu thế giới các bạn - chính là Trái Đất.
            Tôi mong mọi người có thể giúp đỡ tôi phát triển sau này ạ!
        """,
        """
            Xin chào! Đây là NEUTRONS - đến từ lớp 9G.
            Hãy ủng hộ tôi mọi người ơi!
            Tôi mong trong tương lai mọi người sẽ cùng hộ trợ tôi tiến bước phát triển!
        """,
        """
            Tên tôi là NEUTRONS - một trợ lý ảo đến từ lớp 9G.
            Tôi có mong muốn phát triển thêm trong tương lai.
            Từ đó giúp Việt Nam đất nước chúng ta sánh vai với các ông lớn kĩ thuật số trên thế giới!
        """,
        """
            Tôi là NEUTRONS!
            Mong các bạn ủng hộ tôi thật nhiều.
            Chúc ngày hội STEM thành công tốt đẹp!
            Xin cảm ơn các bạn ạ!
        """)

AI_np = ("Không sao","Không sao cả","Không có gì", "Không có chi","Không có gì đâu ạ","Không có chi ạ")

AI_lookup = ("Mời chọn một từ để tra ạ", "Bạn muốn tra từ nào?","Chọn một từ để tra", "Hãy chọn một từ", "Từ nào bạn muốn biết?","Từ nào bạn muốn tra ạ?","Bạn muốn biết từ vựng nào?","Từ mới nào bạn chưa biết?","Hãy nói từ cần tra?", "Tra từ nào?")

AI_welcome = ("Chào bạn!", "Lô!", "Xin chào", "Chào!", "Chào mọi người nha", "Chào đằng ấy","Hola! Haha","Xin chào tất cả mọi người ạ", "Chào mọi người có mặt ở đây", "Chào bạn tôi","Chào nha")

AI_suggest = ("Neutrons có thể giúp gì cho bạn?", "Bạn cần Neutrons làm gì?","Tôi có thể giúp gì cho bạn?", "Bạn có cần tôi giúp không?", "Tôi có thể giúp bạn giờ đây!", "Bạn cần giúp gì?", "Bạn muốn tôi làm gì?","Bạn cần giúp gì không?", "Tôi có thể giúp bạn vài thứ đó!", "Bạn cần gì tôi sẽ giúp!","Bạn cần gì?","Tôi có thể giúp bạn","Cần gì không?","Bạn cần gì không?", "Cần giúp gì chứ?")

AI_sorry = ("Xin lỗi! Nói to lên đi ạ", "Tôi không hiểu ý bạn lắm", "Tôi không biết bạn nói gì", "Xin lỗi, nói to hơn nữa đi ạ!","Xin lỗi, tôi vẫn chưa rõ bạn nói gì!","Nói rõ hơn nữa được không ạ?","Ở đó hơi ồn, tôi không nghe rõ", "Tôi không nghe rõ lắm")

AI_wordmean = ("Nghĩa: ","Từ này nghĩa là ", "Nó có nghĩa ", "À, nghĩa là ", "Đó là ","Định nghĩa: ", "Nghĩa là ","Từ này mang ý nghĩa ","Hmm, nghĩa là ", "","")

AI_bye = ("Tạm biệt đằng ấy","Tôi sẽ nhớ bạn lắm đó", "Tạm biệt!", "Hẹn gặp lại!","Nhớ bạn quá nhưng mà tạm biệt thôi!", "Chào tạm biệt bạn nha","Mong gặp lại sớm!","Xin chào và hẹn gặp lại!")

comeback = ("Đã trở lại", "Mừng trở lại", "Trở lại rồi", "Đã về trang chủ", "Về trang chủ", "Hoàn tất", "Đã xong","Đã về","Về rồi")

ask_hea = ("Nay bạn thấy thế nào?", "Hôm nay bạn khỏe không?", "Bạn khỏe chứ?", "Khỏe không bạn tôi?", "Khỏe chứ?","Sức khỏe dạo này sao rồi?","Khỏe không bạn?","Bạn ổn chứ?")

AI_acp = ("OK!","Ô kê con dê!","Được!","Được thôi!", "Được nha", "OK luôn", "Vâng!", "Được ạ", "Dạ vâng" ,"À à được nhan","Chờ chút nhe")

AI_congrat = ("Tuyệt vời!", "Tốt rồi", "Nghe tuyệt đó", "Vậy tốt quá","Tuyệt nha","Tốt đó", "Tin tốt đó bạn", "Tuyệt khi nghe điều đó", "Tuyệt cú mèo!")

AI_badnew = ("Ồ! Thôi cố lên nha bạn", "Cố lên thôi!", "Cố lên nha bạn ơi", "Ồ buồn thế","Thật buồn khi nghe điều đó!")

AI_ask = ("Dạo này công việc ổn chứ bạn?", "Cuối năm nay thăm tôi nha! Haha","Mọi thứ trong tầm kiểm soát chứ?","Mấy nay mọi cmd thứ thế nào rồi ấy?")

AI_healthsuggest = ("Gác lại mọi thứ và nghĩ dưỡng thôi!", "Bạn nên nghỉ ngơi đi bạn tôi ơi", "Nên nghỉ ngơi nha bạn ơi", "Tạm gác lại mọi thứ và nghỉ ngơi đi bạn", "Ui, tội bạn quá. Nghỉ ngơi thôi bạn ơi!", "Nghỉ ngơi vài ngày là đỡ nha bạn tôi", "Dẹp công việc và nghỉ đê!")

app_name='chrome.exe'

def AFK():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        while True:
            speak(random.choice(AI_ads))
            time.sleep(30)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="vi")
                print("Me:", text)
                if "dừng" in text or "thôi" in text or "quay lại" in text or "đủ rồi" in text:
                    stop()
                    call_infor()
                    call_Jarvis()
                if "Neutrons" in text or "này" in text or "hey" in text:
                    speak("NEUTRONS đây!")
                    time.sleep(2)
                    speak(random.choice(comeback))
                    time.sleep(2)
                    call_Jarvis()
            except sr.UnknownValueError:
                text =""
            except sr.RequestError:
                text=""

def AFKingWeb():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="vi")
                print("Me:", text)
                if "dừng" in text or "thôi" in text:
                    subprocess.Popen(["taskkill", "/f", "/im", app_name])
                    stop()
                    call_Jarvis()
                if "Neutrons" in text or "này" in text or "hey" in text:
                    subprocess.Popen(["taskkill", "/f", "/im", app_name])
                    speak("Neutrons đây!")
                    time.sleep(2)
                    speak(random.choice(comeback))
                    time.sleep(2)
                    call_Jarvis()
            except sr.UnknownValueError:
                text =""
            except sr.RequestError:
                text=""

def call_infor():
    speak(random.choice(AI_welcome))
    time.sleep(1.5)
    speak("Tôi biết tên bạn được không?")
    name = input()
    speak("Rất vui khi gặp bạn, " + str(name))
    time.sleep(2)

def help():
    speak("""Tôi có thể làm như sau:
        1. Trò chuyện với bạn    
        2. Cho biết thời gian
        3. Dự báo thời tiết
        4. Nghe nhạc
        5. Tra từ điển Anh-Việt và Việt-Anh
        6. Thông tin hệ thống
        7. Thời tiết ở thành phố
        8. Tra Wikipedia
        9. Tìm kiếm thông tin Google
        """)
    time.sleep(20)

def qanda():
    text=get_text()
    if "là gì" in text or "cái gì" in text or "thế nào là" in text or "định nghĩa" in text:
        contents=wikipedia.summary(text).split('\n')
        speak((contents[0].split('.'))[0])
        time.sleep((len((contents[0].split('.'))[0])//3))
        call_Jarvis()
    else: google_search()

def wikisearch():
    speak("Bạn muốn biết cái gì?")
    time.sleep(1.5)
    text=get_text()
    contents=wikipedia.summary(text).split('\n')
    speak("Theo tôi biết")
    time.sleep(1.5)
    speak((contents[0].split('.'))[0])
    time.sleep((len((contents[0].split('.'))[0])//3))
    speak("Bạn muốn biết thêm không? Hay quay trở lại?")
    time.sleep(2.5)
    text=get_text()
    if "có" in text or "tiếp" in text or "tiếp tục" in text:
        wikisearch()
    elif "thôi" in text or "dừng" in text or "đủ rồi" in text:
        stop()
        call_Jarvis()

def google_search():
    text=get_text()
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": text
    })
    headers = {
    'X-API-KEY': '77ff8aac8e0b469531d47168e51db80bb02936eb',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    searchresult = (response.text.split('"link":"')[1]).split('","snippet')[0]
    speak("Đây là kết quả tra cứu")
    time.sleep(2)
    webbrowser.open(url)
    AFKingWeb()

def play_youtube():
    speak("Tìm kiếm:")
    time.sleep(3)
    my_song = get_text()
    while True:
        result = YoutubeSearch(my_song, max_results = 10).to_dict()
        if result:
            break;
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Thưởng thức!")
    AFKingWeb()

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow = False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Me: ", end = '')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi")
            print(text)
            return text
        except:
            print("...")
            return ""

def timenow(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d, tháng  %d, năm  %d " % (now.day, now.month, now.year))
        time.sleep(1)
    else:
        speak(randome.choice(AI_sorry))

def stop():
    speak("Đang thoát")
    time.sleep(2)
    speak(random.choice(comeback))
    time.sleep(3)

def end():
    speak("Đang thoát chương trình")
    time.sleep(2)
    speak(random.choice(AI_bye))
    time.sleep(3)
    exit()

def talk():
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng! Chúc bạn một ngày tốt lành!")
    elif day_time < 18:
        speak("Chào buổi chiều!")
    else:
        speak("Chào buổi tối!")
    time.sleep(5)
    speak(random.choice(ask_hea))
    time.sleep(4)
    ans = get_text()
    if ans:
        if "khỏe" in ans or "tốt" in ans or "có" in ans or "ổn" in ans or "được" in ans:
            speak(random.choice(AI_congrat))
            time.sleep(1.5)
        elif "không ổn" in ans or "tệ" in ans or "xấu" in ans or "xuống sức" in ans or "không" in ans or "mệt" in ans or "kiệt sức" in ans:
            speak(random.choice(AI_healthsuggest))
            time.sleep(2)
    speak(random.choice(AI_ask))
    time.sleep(4)
    ans=get_text()
    if ans:
        if "được chứ" in ans or "ok" in ans or "được thôi" in ans or "vẫn ổn" in ans or"cũng ổn" in ans or "cũng được" in ans or "bình thường" in ans or "ổn" in ans:
            speak(random.choice(AI_congrat))
            time.sleep(1)
            call_Jarvis()
        elif "chưa biết" in ans or "không ổn" in ans or "không" in ans or "tùy" in ans or "khó khăn" in ans:
            speak(random.choice(AI_badnew))
            time.sleep(3)
            ans=get_text()
            if "cảm ơn" in ans or "cám ơn" in ans or "thank" in ans:
                speak(random.choice(AI_np))
                time.sleep(2)
                call_Jarvis()
            call_Jarvis()

def weather():
    speak("Bạn muốn biết thời tiết nơi nào?")
    time.sleep(3)
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temp = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        sun_time  = data["sys"]
        sun_rise = datetime.datetime.fromtimestamp(sun_time["sunrise"])
        sun_set = datetime.datetime.fromtimestamp(sun_time["sunset"])
        wther = data["weather"]
        weather_des = wther[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day}, tháng {month}, {year}
        Mặt trời mọc lúc {hourrise}:{minrise} giờ sáng
        Mặt trời lặn lúc {hourset}:{minset} giờ tối
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} (hPa)
        Độ ẩm không khí là {humidity}% """.format(day= now.day, month = now.month, year = now.year, hourrise = sun_rise.hour, minrise = sun_rise.minute, hourset = sun_set.hour, minset = sun_set.minute, temp = current_temp, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(25)
    else:
        speak("Nơi này không khả dụng!")
def system():
    speak("""
        Tên AI: Neutrons
        Tên phần mềm: Trợ lý ROBOT ảo dùng trí tuệ thông minh - bản BETA
        Phiên bản phần mềm: 1.2
        Xuất xứ: Đội ngũ lớp 9G trường Trung Học Cơ Sở Lê Hồng Phong
        Tên tắt: VAR AI
        UID hệ thống: VARAI01052024
        Số SERI: F2RQT9UWH24
        """)

def get_text():
    while True:
        text = get_voice()
        if text:
            return text.lower()

def diclst(file_path):
    doc = Document(file_path)
    lines = []
    for para in doc.paragraphs:
        lines.extend(para.text.split('\n'))
    return lines

def dictionaryVN(text):
    speak(random.choice(AI_lookup))
    time.sleep(3.5)
    text=get_text()
    look_upVN=text.split(": ")
    file_pathVN = 'DICTIONARYDOC.docx'
    linesVN = diclst(file_pathVN)
    if text.split("tra từ")=="" or "dừng lại" in text or "dừng lại" in text or "quay trở lại đi bot" in text or "quay lại" in text:
        stop()
        call_Jarvis()
    for j in range(len(look_upVN)):
        k=0
        print(look_upVN[j].capitalize())
        for i in range(len(linesVN)):
            readVN=linesVN[i].split(": ")
            if look_upVN[j].capitalize() in readVN[-1] or look_upVN[j] in readVN[-1] or look_upVN[j].capitalize() in readVN[-1].capitalize():
                speak(random.choice(AI_wordmean)+str((readVN[0].split(" /")[0]).split(". ")[1]))
                time.sleep(3)
                k+=1
        if k==0: 
            speak(look_upVN[j]+" không có trong từ điển")
            time.sleep(3)

def dictionary(text):
    speak(random.choice(AI_lookup))
    time.sleep(3.5)
    text=get_text()
    look_up=(text.lower()).split(": ")
    file_path = 'DICTIONARYDOC.docx'
    lines = diclst(file_path)
    if text.split("tra từ")=="" or "dừng lại" in text or "dừng lại" in text or "quay trở lại đi bot" in text or "quay lại" in text or "dừng" in text:
        stop()
        call_Jarvis()
    for j in range(len(look_up)):
        k=0
        for i in range(len(lines)):
            read=lines[i].split(" /")
            if look_up[j].capitalize()==str(read[0].split(". ")[-1]):
                speak(random.choice(AI_wordmean)+str(read[1].split(": ")[-1]))
                time.sleep(4)
                k+=1
        if k==0: 
            speak(look_up[j]+" không có trong từ điển")
            time.sleep(3)
def checkdic():
    if "việt anh" in text or "từ điển việt" in text or "tra từ tiếng việt" in text or "từ tiếng việt" in text:
        speak("Chào mừng tới từ điển Việt Anh")
        time.sleep(3)
        while True:
            dictionaryVN(text)
    elif "anh việt" in text or "từ điển anh việt" in text or "tra từ tiếng anh" in text or "từ tiếng anh" in text:
        speak("Chào mừng tới từ điển Anh-Việt!")
        time.sleep(2.5)
        while True:
            dictionary(text)

def call_Jarvis():
    speak(random.choice(AI_suggest))
    time.sleep(2.5)
    while True:
        text = get_text()
        if not text:
            break
        elif "dừng" in text or "tạm biệt" in text or "dừng chương trình" in text or "Hẹn gặp lại Jarvis"in text or "hẹn gặp" in text:
            end()
        elif "giúp gì" in text or "liệt kê tác vụ" in text or "giúp đỡ" in text or "giúp những gì" in text :
            help()
            time.sleep(4)
            call_Jarvis()
        elif "trò chuyện" in text or "nói chuyện" in text or "tám chuyện" in text or "nói với" in text:
            speak("Được thôi")
            time.sleep(0.5)
            talk()
        elif "ai tạo" in text or "bạn đến từ đâu" in text or "Neutrons là ai" in text or "Neutrons là cái gì" in text or "bạn là ai" in text or "là ai" in text or "là gì" in text or "là cái gì" in text or "giới thiệu" in text:
            system()
            time.sleep(35)
            call_Jarvis()
        elif "tra từ điển" in text or "tra từ" in text or "từ điển" in text or "từ mới" in text or "từ vựng mới" in text:
            if "tiếng" in text or "việt" in text or "anh" in text:
                checkdic()
            else:
                speak("Bạn muốn tra từ điển nào? Việt-Anh hay Anh-Việt?")
                time.sleep(3)
                text=get_text()
                checkdic()
        elif "thời tiết" in text or "dự báo thời tiết" in text:
            weather()
            time.sleep(3)
            call_Jarvis()
        elif "giờ" in text or"mấy giờ" in text or "ngày" in text or"ngày bao nhiêu" in text:
            timenow(text)
            time.sleep(3)
            call_Jarvis()
        elif "nhạc" in text or"mở nhạc" in text or "chơi nhạc" in text or "xem youtube" in text:
            while True:
                play_youtube()
        elif "treo máy" in text or "quảng cáo" in text or "trưng bày" in text or "AFK" in text or "afk" in text: 
            AFK()     
        elif "tra định nghĩa" in text or "tìm định nghĩa" in text or "định nghĩa" in text or "thông tin" in text:
            speak(random.choice(AI_acp))
            time.sleep(1)
            wikisearch()
        elif "tìm kiếm" in text or "google" in text or "cách" in text or "tra google" in text:
            google_search()
        else: qanda()             
call_infor()         
call_Jarvis()