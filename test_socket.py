import socket
import sys

def try_port(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	try:
		s.connect(('212.83.175.138', port))
	except socket.error:
		print("port {} closed !!".format(port))
		return False

	try :
		data = s.recv(4096)
		print ("port ouvert et data :{}".format(data))
		return True
	except socket.timeout:
		print("port ouvert mais timeout !!!")
		return True

	s.close()
	return data

# def scan():
# 	found_ports = []
# 	for port in range(1,65535):
# 		connected = try_port(port)
# 		if connected:
# 			found_ports.append(port)
# 	return found_ports

# print scan()
print try_port(int(sys.argv[1]))