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
