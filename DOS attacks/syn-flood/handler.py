import argparse
import textwrap


def args_handler():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        A script for performing a simple Syn Flood Attack on target IP address with multiple threads.
        
        Usage examples:
        1. To perform Syn Flood Attack on the target IP and to the default port (8080) from your default port(7000) and number of threads (500):
           Run: python syn-flood.py 192.168.1.100
        
        2. To specify the target IP to a specified destination port (e.g., 4343) and from your source port(e.g., 9000) and a specified number of threads (e.g., 200):
           Run: python syn-flood.py 192.168.1.100 -dp 4343 -sp 9000 -t 200
        ''')
    )
    
    # Required argument for the target IP address
    parser.add_argument('target_ip', help='Target IP address')
    
    # Optional argument for Destination Port Number (default is 8080)
    parser.add_argument('-dp', '--dport', type=int, default=8080, help='Destination Port Number')
    
    # Optional argument for Source Port Number (default is 7000)
    parser.add_argument('-sp', '--sport', type=int, default=7000, help='Source Port Number')
    
    # Optional argument for the number of threads (default is 1)
    parser.add_argument('-t', '--threads', type=int, default=500, help='Number of threads (default: 500)')
    
    args = parser.parse_args()
    
    
    return args.target_ip, args.dport, args.sport, args.threads