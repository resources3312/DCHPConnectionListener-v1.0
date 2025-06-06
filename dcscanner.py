import sys
import os
from datetime import datetime
from scapy.all import sniff, DHCP


class ARPHandler:
    def __init__(self, interface):
        self.interface = interface
    
    def packetCheck(self, packet):
        try:
            options = packet[DHCP].options
            if options[0][1] == 3: print(f"[{datetime.now().strftime('%H:%M:%S')}] Device: {options[5][1].decode('utf-8')} Address: {options[2][1]}")
        except: pass
    
    def startARPMonitor(self) -> None:
        os.system("clear" if os.name != "nt" else "cls")
        print(f"DCHPConnectionListener v1.0\n{'-' * 50}")
        
        try: sniff(filter="udp and (port 67 or port 68)", prn=self.packetCheck, store=0, iface=self.interface)
        except KeyboardInterrupt: sys.exit("Quitting..")


def getArgument(argument: str) -> str:
    return 

def main() -> None:
    if "--interface" not in sys.argv: sys.exit("Usage: dcscanner --interface <network-interface>")

    scanner = ARPHandler(interface=sys.argv[sys.argv.index("--interface") + 1])
    
    scanner.startARPMonitor()

if __name__ == '__main__': main()
