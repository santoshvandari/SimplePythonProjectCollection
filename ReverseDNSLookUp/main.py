

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