import socket

def client():
    host = '127.0.0.1'  # The server's hostname or IP address
    port = 5000  # The port used by the server

    # Create a socket object and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())

    # Receive the server's response
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    client()
