import socket
from threading import Thread

def run(port):
	sock = socket.socket()
	sock.bind((socket.gethostname(), port))
	sock.listen(3)
	print('Starting server on port {0}'.format(port))

	while True:
		client, address = sock.accept()
		print('Connection from {0}'.format(address))
		client.send('I\'m up!'.encode())
		client.close()

class Server(Thread):

	def __init__(self, port) -> None:
		super().__init__(target=run, args=(port,))
		self.port = port

def main():
	ports = [21, 22, 80, 443]
	for port in ports:
		server = Server(port)
		server.start()


if __name__ == '__main__':
	main()
