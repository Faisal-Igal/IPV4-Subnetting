## this script take a range of IP addresses, identifies which ones are live on the network, then checks to see if they have ports 80, 443, 0r 22 open. 

# Import neccessary libraries
import socket
import ipaddress
import threading

# Define the IP range to scan (e.g., 192.168.1.1 - 192.168.1.254)
ip_range = '192.168.1.1-192.168.1.254'

# Ports to check (80 for HTTP, 443 for HTTPS, 22 for SSH)
ports_to_check = [80, 443, 22]


# function takes an IP address and a list of ports as input
def check_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust the timeout as needed
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


# function takes an IP range and a list of ports as input
def scan_ip_range(ip_range, ports):
    live_ips = []
    for ip in ipaddress.IPv4Network(ip_range, strict=False):
        if check_ping(str(ip)):
            live_ips.append(str(ip))
            open_ports = check_ports(str(ip), ports)
            if open_ports:
                print(f'IP: {ip}, Open Ports: {open_ports}')


# function takes an IP address as input and tries to ping it
def check_ping(ip):
    try:
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            return True
        else:
            return False
    except Exception:
        return False

# Run the IP range scan
scan_ip_range(ip_range, ports_to_check)
