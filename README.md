# 🎓 Examination Proctoring System

An intelligent AI-powered remote proctoring system built using **Flask** and **OpenCV** to ensure fair and secure online examinations.

---

## 🚀 Project Overview

This system monitors candidates during online exams using computer vision and audio detection techniques.  
It detects suspicious activities such as:

- 👥 Multiple faces detection  
- 🚫 Face not visible (moving away from screen)  
- 📱 Mobile phone detection  
- 🔊 Background noise detection  
- ⚠️ Automatic warning system  
- ❌ Auto termination after repeated violations  

The system ensures transparency, fairness, and exam integrity.

---

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Flask
- 📷 OpenCV
- 🤖 Computer Vision
- 🧠 AI-based Detection Modules
- 🎥 Webcam Monitoring
- 🔊 Noise Detection

---

## 🧩 System Modules

### 👤 User Management Module
- Accesses user camera during the exam
- Ensures continuous monitoring

### 📝 Exam Management Module
- Displays questions on screen
- Controls exam flow and timing

### 👁️ Monitoring Module
- Face detection
- Head movement tracking
- Mobile detection
- Noise monitoring

### 📊 Reporting & Alert Module
- Logs suspicious activities
- Sends alerts and warning sounds
- Automatically terminates exam after 2 violations

---

## 📂 Project Structure
Examination-Proctoring-System/
│
├── app.py
├── proctoring/
│ ├── face_detection.py
│ ├── head_movement.py
│ ├── mobile_detection.py
│ ├── noise_detection.py
│ └── logger.py
│
├── questions/
│ └── python_questions.py
│
├── templates/
│ ├── home.html
│ ├── exam.html
│ └── completed.html
│
└── README.md

## ⚙️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/CodeHarsha123/Examination-Proctoring-System.git
2️⃣ Navigate to Folder
cd Examination-Proctoring-System
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python app.py

Open browser and go to:

http://127.0.0.1:5000
🔮 Future Enhancements

🧑‍💻 Face Recognition Authentication

👀 Advanced Eye Tracking

☁️ Cloud Deployment

📊 Admin Analytics Dashboard

🔐 Stronger AI-based Behavior Analysis

🎯 Conclusion

This project demonstrates how Artificial Intelligence and Computer Vision can enhance the security of online examinations by reducing malpractice and ensuring a fair testing environment.
