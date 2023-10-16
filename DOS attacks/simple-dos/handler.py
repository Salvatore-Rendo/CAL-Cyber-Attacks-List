import argparse
import textwrap


def args_handler():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        A script for performing a simple DoS Attack on target IP address with multiple threads.
        
        Usage examples:
        1. To perform DoS Attack on the target IP and with the default destiantion port (8080) and number of threads (500):
           Run: python simple-dos.py 192.168.1.100
        
        2. To specify the target IP at specified destination port (e.g., 4343) and the number of threads (e.g., 200):
           Run: python simple-dos.py 192.168.1.100 -dp 4343 -t 200
        ''')
    )
    
    # Required argument for the target IP address
    parser.add_argument('target_ip', help='Target IP address')
    
    # Optional argument for port number (default is 8080)
    parser.add_argument('-dp', '--dport', type=int, default=8080, help='Destination Port Number (default: 8080)')
    
    # Optional argument for the number of threads (default is 1)
    parser.add_argument('-t', '--threads', type=int, default=500, help='Number of threads (default: 500)')
    
    args = parser.parse_args()
    
    
    return args.target_ip, args.dport, args.threads