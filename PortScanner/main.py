import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

ipaddress=input("Enter the IP address: ")
try:
    socket.inet_aton(ipaddress)
except socket.error:
    print("Invalid IP Address")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {ipaddress}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ipaddress, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program!")
    sys.exit()
except socket.gaierror:
    print("\nHostname Could Not Be Resolved!")
    sys.exit()
except socket.error:
    print("\nServer not responding!")
    sys.exit()
