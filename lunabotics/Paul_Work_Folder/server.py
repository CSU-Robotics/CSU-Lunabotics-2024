import socket
import subprocess

def get_ip_address():
    # Run a command to get the IP address
    result = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
    ip_address = result.stdout.decode().strip()
    return ip_address

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Server listens on all interfaces on port 12345
    server_socket.listen(1)  # Listen for one incoming connection

    print("Server listening for connections...")

    client_socket, client_address = server_socket.accept()
    print("Connection established with:", client_address)

    # Get the server's IP address
    server_ip = get_ip_address()
    client_socket.sendall(server_ip.encode())  # Send the IP address to the client

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received:", data.decode())

    print("Connection closed.")
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server()