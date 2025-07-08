from voice import speak, get_text
from docx import Document
import time

def diclst(file_path):
    doc = Document(file_path)
    return [p.text for p in doc.paragraphs if p.text]

def check_dictionary():
    speak("Bạn muốn tra từ điển Anh-Việt hay Việt-Anh?")
    kind = get_text()

    speak("Hãy nói từ cần tra:")
    word = get_text()
    path = "DICTIONARYDOC.docx"
    lines = diclst(path)
    found = False

    for line in lines:
        if word.lower() in line.lower():
            speak("Kết quả: " + line)
            found = True
            break

    if not found:
        speak("Không tìm thấy từ trong từ điển.")
