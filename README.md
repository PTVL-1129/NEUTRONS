# 🤖 NEUTRONS - Vietnamese AI Virtual Assistant

![Clone repo](https://github.com/PTVL-1129/NEUTRONS.git)
---

## 🧠 Giới thiệu

**NEUTRONS** là một **trợ lý ảo tiếng Việt** đầu tiên được xây dựng bởi học sinh lớp 9G, được phát triển với mục tiêu:
- Học hỏi lập trình Python từ con số 0
- Kết hợp nhiều thư viện hiện đại: **speech recognition**, **wikipedia API**, **web automation**, **dictionary**, v.v.
- Tích hợp **AI giọng nói** và giao tiếp **tự nhiên bằng tiếng Việt**

> Dù là phiên bản đầu tay, NEUTRONS vẫn mang tham vọng trở thành nền móng cho các dự án robot – AI sau này!

---

## 🧩 Tính năng nổi bật

| 💡 Tính năng | 🔍 Mô tả |
|-------------|----------|
| 🎙️ Nhận diện giọng nói | Sử dụng Google Speech Recognition để hiểu tiếng Việt |
| 🗣️ Phản hồi bằng giọng nói | Dùng `gTTS` để phát âm giống người thật |
| 🔎 Tra từ điển Anh–Việt / Việt–Anh | Hỗ trợ đọc định nghĩa từ file `.docx` |
| 🌐 Tra cứu Wikipedia | Tóm tắt thông tin tiếng Việt từ Wikipedia |
| ☀️ Dự báo thời tiết | Sử dụng API của OpenWeatherMap |
| 🔍 Tìm kiếm Google | Gửi query đến API tìm kiếm Serper |
| 📺 Mở nhạc YouTube | Tìm kiếm và phát bài hát trực tiếp từ YouTube |
| 🧾 Trò chuyện thân thiện | Chào hỏi, hỏi thăm, tạm biệt như một người bạn |

---

## 🛠️ Các công nghệ đã dùng
speech_recognition – Nhận diện giọng nói
gTTS + playsound – Tạo giọng nói tiếng Việt
wikipedia – Tra cứu kiến thức
selenium – Mở trình duyệt và tự động thao tác
requests – Gửi API truy vấn Google
docx – Đọc file từ điển .docx
datetime, os, subprocess – Xử lý hệ thống

---

## 💬 Một số câu lệnh mẫu
"Tra từ điển" → Bắt đầu tra từ Anh–Việt hoặc Việt–Anh
"Neutrons ơi" → Gọi trợ lý
"Thời tiết ở Hà Nội" → Xem nhiệt độ, độ ẩm,...
"Mở nhạc [tên bài]" → Phát YouTube
"Tra Google [từ khoá]" → Mở tìm kiếm trên Chrome
"Hẹn gặp lại" / "Tạm biệt" → Thoát chương trình

---

## 🧠 Về nhóm phát triển
Dự án được xây dựng bởi 2 học sinh Phạm Thế Vũ Lâm và Lục Trần Bình Minh, lớp 9G, trường THCS Lê Hồng Phong, phường An Khê, tỉnh Gia Lai, Việt Nam. Với đam mê học lập trình từ những dòng code đầu tiên.

“Chúng tôi bắt đầu từ con số 0 – nhưng với quyết tâm tạo ra điều gì đó có ích, vui nhộn và học hỏi được thật nhiều.”

---

## 🚀 Định hướng tương lai
Kết nối với robot thật
Giao tiếp bằng camera & nhận diện khuôn mặt
Chuyển sang dùng ChatGPT API để phản hồi thông minh hơn
Xây dựng giao diện GUI đẹp mắt

---

## 📜 Giấy phép
Dự án chia sẻ với mục đích học tập – phi lợi nhuận. Ai cũng có thể clone và mở rộng lại.

## 🙏 Cảm ơn bạn đã ghé thăm NEUTRONS!
Nếu bạn thích dự án, đừng quên ⭐ star và để lại góp ý nhé!

## 📁 Cấu trúc dự án

```bash
NEUTRONS/
├── src/
│   ├── main.py               # File chạy chính
│   ├── dictionary.py         # Xử lý tra từ
│   ├── voice.py              # Xử lý giọng nói
│   ├── search.py             # Xử lý tra cứu thông tin
│   ├── utils.py              # Tiện ích chung
├── data/
│   └── DICTIONARYDOC.docx    # Từ điển 5000 từ vựng
├── requirements.txt
└── README.md
└── .gitignore

