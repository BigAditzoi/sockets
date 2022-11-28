from threading import Thread
import socket
import time

servers = {21: False, 22: False, 80: False, 443: False}


def run(port):

	sock = socket.socket()
	sock.connect((socket.gethostname(), port))
	response = sock.recv(1024).decode()

	if response == 'I\'m up!':
		servers[port] = True
	else:
		print(response)

	sock.close()


def main():

	for port in servers:
		thread = Thread(target=run, args=(port,))
		thread.start()

	time.sleep(1)
	print(servers)


if __name__ == '__main__':
	main()