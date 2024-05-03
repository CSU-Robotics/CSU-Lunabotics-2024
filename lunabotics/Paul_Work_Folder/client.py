import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('<server_ip>', 12345)  # Replace '<server_ip>' with the IP address of Raspberry Pi 1
    client_socket.connect(server_address)

    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message == 'exit':
            break
        client_socket.sendall(message.encode())

    print("Closing connection...")
    client_socket.close()

if __name__ == "__main__":
    client()