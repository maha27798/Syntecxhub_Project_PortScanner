import socket
import threading
import argparse
from datetime import datetime

print_lock = threading.Lock()

def scan_port(host, port, logfile):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((host, port))

        with print_lock:
            if result == 0:
                print(f"[OPEN] Port {port}")
                logfile.write(f"[OPEN] Port {port}\n")
            else:
                logfile.write(f"[CLOSED] Port {port}\n")

        s.close()

    except Exception as e:
        with print_lock:
            logfile.write(f"[ERROR] Port {port} : {e}\n")

def main():
    parser = argparse.ArgumentParser(description="Multithreaded TCP Port Scanner")
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print("Host resolve error")
        return

    print(f"Scanning target: {target_ip}")
    print(f"Time started: {datetime.now()}")

    logfile = open("scan_results.txt", "w")

    threads = []

    for port in range(args.start_port, args.end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port, logfile))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    logfile.close()

    print(f"Scan completed: {datetime.now()}")

if __name__ == "__main__":
    main()
