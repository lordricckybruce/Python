#!/usr/bin/env python3
'''
import socket   #socket module for networking
import threading   #threading allows server handle multiple clients

def handle_client(client_socket): #a functio  for handle client for all connected client
    """Function to handle client connections."""
    while True:  #an indefinite loop and designed to continously listen to for icoming messgaes from connected client
        try:  #that the server can handle errors withput  crashing, maintaining the server stability
            message = client_socket.recv(1024).decode('utf-8')
            if not message:  # If no message is received, client has disconnected
                break
            print(f"Received: {message}")  #print message
            # Echo the message back to the client
            client_socket.send(f"Echo: {message}".encode('utf-8'))
        except ConnectionResetError:  #if client forcly closes connection while server is trying to read from the socket
            break

    client_socket.close()  #closes connection
    print("Client disconnected.")
#defining a tcp server scocket
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
 #handle_client=to call a new thread args = passes the client_socket to handle_socket
        client_handler.start()  #creates thread for new connection

if __name__ == "__main__":
    tcp_server()


import socket #a module to create and manage network
import threading #a module to handle mutiple client at once
def handle_client(client):  #handle_client takes a single argument client, the purpose is to handle 
				communication between server and client(send and receive messages)
	while True:      #an infinite loop that keeis the server lsitening to specific  client for incoming messages from different client
		try:   #this watches out for error, even if a client disconnects it doesn't crash the server
			message = client.recv(1024).decode('utf-8') 
			 #message is received and utf-8 coverts them from bytes into readable messages
			if not message:     #if the message is empty it means client disconnected
				break      #stops while loop from listening since client disconnected
			print(f'Received: {message}') #print message
			client.send(f'Echo: {message}'.encode('utf-8')) #echo message of client
		except ConnectionResetError: #client not connected with server
			break   #server disconnects with the client
	client.close() #close connection
	print("Client disconnected")
def tecp_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('localhost', 8080))
	server_socket.listen(1)
	print("TCP server lsitening on port 8080")
	while True:
		client_socket, client_address = server_socket.accept()
		print(f'Connection established with {client_address}')
		client_handler =  threading.Thread(target=handle_client, args=(client_socket))
		client_handler.start()
if __name__ == "__main__":
	tccp_server()
'''
import socket
import threading
def handle_client(client_socket):
	while True:
		try:
			message = client_socket.recv(1024).decode('utf-8')
			if not message:
				break
			print(f'Received:  {message}')
			client_socket.send(f'Echo: {message}'.encode('utf-8'))
		except ConnectionResetError:
			break
	client_socket.close()
	print("Client Disconnected")
def tcp_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 8080))
	server.listen(19)
	while True:
		client_socket, client_address = server.accept()
		print(f'Connectio  etsablished with {client_address}')
		
		clinet_handler =threading.Thread(target=handle_client, args=(client_socket))
		client_handler.start()
if __name__ == "__main__":
	tcp_server()
