from random import *

def fake_ip_gen():
	while True:
		ip_bytes = [str(randrange(0,256)) for i in range(4)]
		if ip_bytes[0] == "127":
			continue
		fake_ip = '.'.join(ip_bytes)
		break
	return fake_ip