#!/bin/python3
import socket
'''
def start_tcp_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('localhost', 8080))
	message = client.recv(1024)
	print(f'Received from server: {message.decode()}')
	client.close()
if __name__ == "__main__":
	start_tcp_client()


def client():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('localhost', 9090))
	message = client_socket.recv(1024)
	print(f'Received from server: {message.decode()}')
	client_socket.close()
if __name__ == "__main__":
	client()

def tcp_client():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('localhost', 9091))
	message = client_socket.recv(1024)
	print(f'Received from server: {message.decode()}')
	client_socket.close()
if __name__ == "__main__":
	tcp_client()

import socket

def tcp_client():
    """Function to set up the TCP client."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    while True:
        message = input("Enter a message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    client_socket.close()

if __name__ == "__main__":
    tcp_client()


import socket
def tcp_client():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('localhost', 9090))
	message = client_socket.recv(1024)
	print(f'Receievd from server: {message.decode()}')
	client_socket.close()
if __name__ == "__main__":
	tcp_client()
'''
import socket
def tcp_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('localhost', 7070))
	message = client.recv(1024)
	print(f'Received from server: {message.decode()}')
	client.close()
if __name__ == "__main__":
	tcp_client()
