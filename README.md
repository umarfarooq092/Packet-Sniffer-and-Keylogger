Network Sniffer and Keylogger Simulation

This repository contains two Python-based cybersecurity projects aimed at enhancing the understanding of network traffic analysis and keystroke logging techniques. These projects were developed for educational purposes to help build a strong foundation in network security and ethical hacking.

Project 1: Network Sniffer in Python

A network sniffer that captures and analyzes real-time network traffic. This tool uses the Scapy library to intercept IP packets and TCP/UDP traffic, displaying relevant packet information such as source and destination IPs, and port numbers. The sniffer is designed to work with elevated privileges (e.g., sudo) and logs captured data with timestamps for later analysis.

Key Features:

Capture and analyze real-time network traffic.

Focus on TCP and UDP protocols for packet sniffing.

Log captured packet details (source IP, destination IP, port numbers).

Safe execution with interrupt support (Ctrl+C).

Technologies Used:

Python

Scapy (for packet sniffing and analysis)

Logging module (for logging packet details)

Project 2: Keylogger Simulation in Python

A simulation of a keylogger to monitor and record keystrokes in a secure, offline environment. The keylogger logs key presses (including special keys) with timestamps and stores the data in a structured CSV file. The program allows for safe exit via the ESC key.

Key Features:

Monitors and logs keyboard inputs in real time.

Logs keys with timestamps and special key formatting (e.g., [ENTER], [SPACE]).

Stores logs in CSV format for easy review.

Safe exit via the ESC key.

Technologies Used:

Python

pynput (for keyboard input monitoring)

CSV module (for log file storage)

Ethical Considerations:

This project was developed for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. The aim is to understand potential security threats and explore defensive strategies within the cybersecurity field.

Learning Outcomes:

Gained practical experience in live traffic monitoring and protocol analysis.

Developed insights into the ethical and legal aspects of keystroke logging and network sniffing.

Strengthened Python programming and system-level scripting skills.

Enhanced awareness of cybersecurity risks such as data theft, identity theft, and unauthorized access.

These projects were completed as part of an internship at Arch Technologies and have deepened my interest in cybersecurity, particularly in network security, digital forensics, and ethical hacking.

Feel free to clone, fork, or contribute to this repository!
