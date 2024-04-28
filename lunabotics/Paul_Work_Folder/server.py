import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345  # Arbitrary non-privileged port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for connections...")

# Accept a connection
client_socket, client_address = server_socket.accept()

print("Connection established with:", client_address)

# Echo back received data
while True:
    data = client_socket.recv(1024)
    if not data:
            break
            print("Received:", data.decode())
            client_socket.sendall(data)

            # Close the connection
            client_socket.close()
