

# Syntecxhub Project - TCP Port Scanner

## Overview
This project is a **Multithreaded TCP Port Scanner** developed using Python.  
The scanner checks open ports on a target host (IP address or domain) and logs the scanning results into a file.

This project demonstrates the use of:
- Python socket programming
- Multithreading (concurrency)
- Exception handling
- Logging scan results
- Command-line arguments

## Features
- Scan a single host
- Scan a range of TCP ports
- Multithreaded scanning for faster performance
- Displays open ports on the terminal
- Logs results into `scan_results.txt`
- Supports both domain names and IP addresses

## Requirements
- Python 3.x

## Usage

Run the scanner using:

```bash
python port_scanner.py <host> <start_port> <end_port>
````

Example:

```bash
python port_scanner.py example.com 1 1000
```

## Output

* Open ports will be displayed on the screen
* All scan results will be saved in `scan_results.txt`
* 
## Screenshots

<img width="1203" height="466" alt="Screenshot 2026-02-09 185952" src="https://github.com/user-attachments/assets/3de8c919-ad4d-4850-97e1-6ba7c6eb7805" />

<img width="1919" height="1152" alt="Screenshot 2026-02-09 190011" src="https://github.com/user-attachments/assets/cfa5b764-3e23-4904-8a9f-efd149a033bc" />

<img width="1920" height="1200" alt="Screenshot 2026-02-09 190025" src="https://github.com/user-attachments/assets/bb50bd2f-f14c-441a-8deb-b14e7fcd8079" />





