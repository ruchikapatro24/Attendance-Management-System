# 📋 Attendance Management System with Face Recognition

A Python-based desktop application that automates recording student attendance using face recognition. Built with Tkinter for the GUI, OpenCV for face detection/recognition, and MySQL for data storage.

![Screenshot](https://github.com/ruchikapatro24/Attendance-Management-System/blob/5712442ee3e6a0b147b2db2ffe430b7c8958eea4/ss.jpg)

---

## 🔍 Project Overview

Students’ faces are enrolled by capturing multiple samples via webcam. The system trains an LBPH face recognizer on these samples and then, during class, scans live video to identify each student and log their attendance automatically to a CSV file and MySQL database.

---

## ✨ Key Features

- **Student Enrollment**  
  Capture 100 face images per student, store metadata (ID, name, roll, department, etc.).

- **Dataset Training**  
  Train an LBPH face recognizer (`classifier.xml`) on collected samples.

- **Live Recognition & Logging**  
  Recognize faces in real time, display name/ID overlay, and mark “Present” with timestamp.

- **Attendance Reports**  
  View, import, export, and update attendance records via a sortable, scrollable table.

- **User-Friendly GUI**  
  Intuitive interface built with Tkinter: enrollment form, training button, recognition button, and report management.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **GUI:** Tkinter  
- **Face Recognition:** OpenCV (LBPH + Haar Cascade)  
- **Database:** MySQL (via `mysql-connector-python`)  
- **Storage:** CSV export/import for reports  
- **Imaging:** Pillow (PIL)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ruchikapatro24/Attendance-Management-System.git
cd Attendance-Management-System
