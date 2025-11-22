from scapy.all import sniff, IP, TCP, UDP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Packet processing function
def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        logging.info(f"[IP] {ip_layer.src} -> {ip_layer.dst}")

        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            logging.info(f"    [TCP] Port: {tcp_layer.sport} -> {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            logging.info(f"    [UDP] Port: {udp_layer.sport} -> {udp_layer.dport}")

# Filter for only IP packets with TCP or UDP
packet_filter = "ip and (tcp or udp)"

def main():
    print("[*] Starting packet capture. Press Ctrl+C to stop...")
    try:
        sniff(filter=packet_filter, prn=process_packet, store=False)
    except PermissionError:
        print("[!] You need to run this script with elevated privileges (e.g., sudo).")
    except KeyboardInterrupt:
        print("\n[!] Packet sniffing stopped by user.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()

