from scapy.all import sniff, ARP, IP

def packet_callback(packet):
    if packet.haslayer(ARP):
        print(f"[ARP] {packet.psrc} is asking for {packet.pdst}")
    elif packet.haslayer(IP):
        print(f"[IP] {packet.src} → {packet.dst} | Protocol: {packet.proto} | Length: {len(packet)} bytes")

sniff(prn=packet_callback, count=10)
