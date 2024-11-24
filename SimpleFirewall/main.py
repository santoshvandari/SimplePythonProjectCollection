from scapy.all import sniff, IP, TCP, UDP

# Define blocking rules
BLOCKED_IPS = ["192.168.1.10", "10.0.0.2"]
BLOCKED_PORTS = [80, 443]  # Block HTTP and HTTPS

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

# Start sniffing (requires root access)
print("Starting the firewall...")
sniff(filter="ip", prn=packet_callback, store=0)
