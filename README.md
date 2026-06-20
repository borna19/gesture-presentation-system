# 🖐️ Gesture Presentation System

## 📖 Project Overview

The **Gesture Presentation System** is an AI-powered computer vision application that allows users to control presentation slides using simple hand gestures. By utilizing a webcam, the system detects hand movements in real time and translates them into presentation commands such as moving to the next slide, returning to the previous slide, or interacting with presentation content without touching a keyboard or mouse.

The project is built using **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI** to provide accurate hand tracking and gesture recognition. It offers a touchless and interactive way to deliver presentations, making it ideal for classrooms, seminars, meetings, and smart presentation environments.

---

# ✨ Features

* 🎥 Real-Time Webcam Detection
* ✋ Accurate Hand Tracking
* 👆 Gesture-Based Slide Navigation
* ⏭️ Next Slide Control
* ⏮️ Previous Slide Control
* ⚡ Fast Gesture Recognition
* 🤖 AI-Powered Hand Landmark Detection
* 🖥️ Easy-to-Use Interface
* 💻 Cross-Platform Support

---

# 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* Flask
* HTML5
* CSS3

---

# 📂 Project Structure

```text
gesture-presentation-system/

├── app.py
├── hand_detector.py
├── gesture_controller.py
├── presentation_control.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Installation Steps

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gesture-presentation-system.git

cd gesture-presentation-system
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install flask
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

---

## 5. Run the Application

```bash
python app.py
```

---

# ⚙️ Working Process

1. Launch the application.
2. The webcam captures the user's hand in real time.
3. OpenCV processes each video frame.
4. MediaPipe detects the hand and its 21 landmarks.
5. The system recognizes predefined hand gestures.
6. Detected gestures are converted into presentation commands.
7. Slides are controlled automatically without using a keyboard or mouse.

---

# 🖐️ Supported Gestures

* 👍 Next Slide
* 👈 Previous Slide
* ✋ Open Hand Detection
* ☝️ Finger Gesture Recognition

*(Modify this section based on the gestures implemented in your project.)*

---

# 🎯 Applications

* Smart Classroom Presentations
* Business Meetings
* Online Teaching
* Touchless Presentation Control
* Interactive Seminars
* AI-Based Human-Computer Interaction
* Computer Vision Learning

---

# 🚀 Future Enhancements

* Laser Pointer Using Finger Tracking
* Virtual Whiteboard
* Annotation on Slides
* Voice Command Integration
* Gesture Customization
* Multi-Hand Gesture Recognition
* AI-Based Gesture Classification

---

# 📸 Screenshots

Add screenshots of your application here.

```
screenshots/

home.png
gesture-control.png
```

---

# 📋 Requirements

* Python 3.10+
* Flask
* OpenCV
* MediaPipe
* PyAutoGUI

---

# 👨‍💻 Author

**Developed by:**
**Barnali Bhowmik**

---

# 📄 License

This project is created for educational and learning purposes. Feel free to modify and improve it as needed.

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub. Your support motivates me to create more AI and Computer Vision projects.
