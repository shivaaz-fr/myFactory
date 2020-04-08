import socket

def get_port_list():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	try:
		s.connect(('163.172.228.224', 1337))
	except socket.error:
		print("port ferme !!!")
		return False

	try:
		s.send("a")
		print s.recv(4096)
	except:
		print("error d'envoi/rececption de data")

	s.close

get_port_list()







# import requests
# url = "http://ctf06.root-me.org:1337"
# # url = "http://cbhfldkwrmnstzvx.neverssl.com/online"

# etat = 0

# while etat < 3:
# 	try:
# 		res = requests.get(url,timeout=0.5)
# 		print (res.text)
# 		etat = 3
# 	except:
# 		print("pas de reponse")
# 		etat+=1