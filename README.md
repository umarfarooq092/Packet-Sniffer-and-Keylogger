# **Network Sniffer and Keylogger Simulation**

This repository contains two **Python-based cybersecurity projects** designed to help understand **network traffic analysis** and **keystroke logging** techniques. These projects were developed for educational purposes, providing a solid foundation in **network security** and **ethical hacking**.

---

## **Project 1: Network Sniffer in Python**

A **network sniffer** that captures and analyzes **real-time network traffic**. This tool uses the **Scapy** library to intercept **IP packets** and **TCP/UDP traffic**, displaying relevant packet information such as **source IP**, **destination IP**, and **port numbers**. The sniffer requires **elevated privileges** (e.g., `sudo`) and logs captured data with **timestamps** for later analysis.

### **Key Features:**
- **Capture and analyze real-time network traffic**.
- Focus on **TCP** and **UDP protocols** for packet sniffing.
- **Log captured packet details** including:
  - **Source IP**
  - **Destination IP**
  - **Port numbers**
- **Interrupt safely** using `Ctrl+C`.
- **Timestamped logs** for later analysis.

### **Technologies Used:**
- **Python**
- **Scapy**: For packet sniffing and analysis
- **Logging module**: For logging packet details

---

## **Project 2: Keylogger Simulation in Python**

A simulation of a **keylogger** designed to monitor and record **keystrokes** in a **secure, offline environment**. This tool logs all key presses (including special keys like **[ENTER]**, **[SPACE]**) with **timestamps** and stores the data in a structured **CSV file**. The program allows for a **safe exit** using the **ESC key**.

### **Key Features:**
- **Monitor and log keyboard inputs** in real-time.
- **Format special keys** such as `[ENTER]`, `[SPACE]` with proper representation.
- Store keystrokes in **CSV format** for easy review and analysis.
- **Safe exit** by pressing the **ESC key**.

### **Technologies Used:**
- **Python**
- **pynput**: For monitoring keyboard input
- **CSV module**: For structured log file storage

---

## **Ethical Considerations**

This project was developed **for educational purposes only**. Unauthorized use of keyloggers is both **illegal** and **unethical**. The goal of this project is to understand potential **security threats**, the implications of **keystroke logging**, and how to build **defensive strategies** within the cybersecurity field.

---

## **Learning Outcomes**
Through these projects, I have:
- Gained **practical experience** in **live traffic monitoring** and **protocol analysis**.
- Developed insights into the **ethical** and **legal aspects** of both **keystroke logging** and **network sniffing**.
- Strengthened **Python programming** and **system-level scripting** skills.
- Enhanced awareness of **cybersecurity risks** such as:
  - **Data theft**
  - **Identity theft**
  - **Unauthorized access**

These projects were completed as part of an **internship at Arch Technologies**, and they have deepened my interest in **cybersecurity**, particularly in **network security**, **digital forensics**, and **ethical hacking**.

---

### **Feel free to clone, fork, or contribute to this repository!**

---
