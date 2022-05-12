import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore

colorama.init()

kprint_lock = threading.Lock()

ip = input('Enter the IP/website to scan: ')
num_prt = int(input('Enter maximum amount of ports to scan (Up to 65,535): '))
print("Now Scanning: " + ip)

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
    except:
        pass


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(num_prt):
        executor.submit(scan, ip, port + 1)
print("Scan Complete")