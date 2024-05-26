# Write a Python program that takes an IP address as input and performs a reverse DNS lookup to find the domain name associated with the IP address. The program should print the domain name if it is found, and an error message if the domain name is not found.

import socket
def reverse_dns_lookup(ip_address):
    try:
        host = socket.gethostbyaddr(ip_address)
        return host[0]
    except socket.herror as e:
        return f"Error performing reverse DNS lookup: {e}"

def Main():
    ip_address = input("Enter an IP address: ")
    domain_name = reverse_dns_lookup(ip_address)
    print(f"Domain name associated with {ip_address}: {domain_name}")

if __name__ == "__main__":
    Main()