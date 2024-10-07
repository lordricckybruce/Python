#!/usr/bin/env python3

import socket
'''
def start_tcp_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 8080))
	server.listen(5)
	print("Tcp listening on port  8080")
	while True:
		client_socket, client_address = server.accept()
		print(f'Connetcion with established with {client_address}')
		client_socket.send(b'Helloa amigo')
		client_socket.close()
if __name__ == "__main__":
	start_tcp_server()

def server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('localhost', 9090))
	server_socket.listen(5)
	print('TCP server listening on port 9090')
	while True:
		client_socket, client_address = server_socket.accept()
		print(f'Connection established with {client_address}')
		client_socket.send(b'Holla amigo')
		client_socket.close()
if __name__ == "__main__":
	server()
'''
'''
def tcp_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 9091))
	server.listen(8)
	print("TCP server is active on port 9091")
	while True:
		client_socket, client_address = server .accept()
		print(f'Connection established with {client_address}')
		client_socket.send(b'Come oh spirit come')
		client_socket.close()
if __name__ == "__main__":
	tcp_server()


#for multiple client

import socket #to import the socket module
import threading #enables connection of multiple clients

def handle_client(client_socket):
    """Function to handle client connections."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:  # If no message is received, client has disconnected
                break
            print(f"Received: {message}")
            # Echo the message back to the client
            client_socket.send(f"Echo: {message}".encode('utf-8'))
        except ConnectionResetError:
            break

    client_socket.close()
    print("Client disconnected.")

def tcp_server():
    """Function to set up the TCP server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Server is listening on port 8080...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    tcp_server()

#fire wall
import socket

def simple_firewall(blocked_ips):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("Firewall active and listening on port 8080")

    while True:
        client_socket, client_address = server_socket.accept()
        if client_address[0] in blocked_ips:
            print(f"Blocked connection attempt from {client_address[0]}")
            client_socket.close()
        else:
            print(f"Accepted connection from {client_address[0]}")
            client_socket.send(b'You are connected to the server!')
            client_socket.close()

if __name__ == "__main__":
    blocked_ips = ['192.168.1.100', '192.168.1.101']
    simple_firewall(blocked_ips)



import socket
def tcp_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 9090))
	server.listen(6)
	print('TCP server lsitening on port 9090')
	while True:
		client_socket, client_address = server.accept()
		print('Connection established with {client_address}')
		client_socket.send(b'Hola')
		client_socket.close()
if  __name__ == "__main__":
	tcp_server()
'''
import socket
def tcp_server():
	server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 7070))
	server.listen(5)
	print("TCP server listening on port 7070")
	while True:
		client_socket, client_address = server.accept()
		print("Connection established with {client_address}")
		client_socket.send(b'Hello world')
		client_socket.close()
if __name__ == "__main__":
	tcp_server()
