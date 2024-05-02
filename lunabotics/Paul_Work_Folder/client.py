import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Use a public IP address to make a connection, the connection is not established.
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except Exception as e:
        print("Error:", e)
        ip_address = None
    finally:
        s.close()
    return ip_address

# Server configuration
SERVER_HOST = get_ip_address()  # IP address of the server
SERVER_PORT = 12345  # Same port as the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send data to the server
while True:
    message = input("Enter message to send (type 'exit' to quit): ")
    if message.lower() == 'exit':
            break
            client_socket.sendall(message.encode())

            # Receive data from the server
            received_data = client_socket.recv(1024)
            print("Received from server:", received_data.decode())

        # Close the connection
    client_socket.close()
