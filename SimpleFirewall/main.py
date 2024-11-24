from scapy.all import sniff, IP, TCP, UDP

# Define blocking rules (can be extended to take user input)
BLOCKED_IPS = []
BLOCKED_PORTS = []

def get_user_input():
    """
    Function to collect user-defined blocked IPs and Ports.
    """
    print("Enter the IP addresses to block (separate by commas):")
    user_ips = input().strip().split(',')
    global BLOCKED_IPS
    BLOCKED_IPS = [ip.strip() for ip in user_ips if ip.strip()]

    print("Enter the ports to block (separate by commas):")
    user_ports = input().strip().split(',')
    global BLOCKED_PORTS
    BLOCKED_PORTS = [int(port.strip()) for port in user_ports if port.strip().isdigit()]

    print(f"Blocked IPs: {BLOCKED_IPS}")
    print(f"Blocked Ports: {BLOCKED_PORTS}")

def packet_callback(packet):
    """
    Callback function to process each captured packet.
    """
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Check if the packet is from/to a blocked IP
        if src_ip in BLOCKED_IPS or dst_ip in BLOCKED_IPS:
            print(f"[BLOCKED] Packet from {src_ip} to {dst_ip}")
            return  # Drop the packet (do nothing)

        # Check if the packet is using a blocked port
        if TCP in packet or UDP in packet:
            dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport
            if dst_port in BLOCKED_PORTS:
                print(f"[BLOCKED] Packet from {src_ip} to {dst_ip} on port {dst_port}")
                return  # Drop the packet (do nothing)

        # Allow other packets
        print(f"[ALLOWED] Packet from {src_ip} to {dst_ip}")

def start_firewall():
    """
    Function to start sniffing network packets.
    """
    print("Starting the firewall...")
    sniff(filter="ip", prn=packet_callback, store=0)

if __name__ == "__main__":
    get_user_input()  # Collect user-defined IPs and Ports to block
    start_firewall()  # Start packet sniffing and filtering
