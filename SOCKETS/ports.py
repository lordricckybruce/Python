import socket

def scan_ports(target_ip):
    print(f"Scanning {target_ip} for open ports...")
    open_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_ip = '192.168.1.1'
    open_ports = scan_ports(target_ip)
    print(f"Open ports on {target_ip}: {open_ports}")
