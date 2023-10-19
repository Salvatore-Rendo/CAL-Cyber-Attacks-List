import argparse
import textwrap


def args_handler():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        A script for performing a Smurf Attack on target IP address with multiple threads.
        For this attack you need to know the victim IP addr and use as the Target IP
        
        Usage examples:
        1. To perform Smurf Attack on the target IP with a standard number of threads (500):
           Run: python smurf-attack.py 192.168.1.100
        
        2. To specify the target IP with a specified number of threads (e.g., 200):
           Run: python smurf-attack.py 192.168.1.100 -t 200
        ''')
    )
    
    # Required argument for the target IP address
    parser.add_argument('target_ip', help='Target IP address')
    
    # Optional argument for the number of threads (default is 1)
    parser.add_argument('-t', '--threads', type=int, default=500, help='Number of threads (default: 500)')
    
    args = parser.parse_args()
    
    
    return args.target_ip, args.threads