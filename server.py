import socket

def server():
    host = '127.0.0.1'  # Localhost
    port = 5000  # Port to bind the server to (changed to 5000)

    # Create a socket object and bind it to the address and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established!")

        # Receive the message from the client
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")

        # Send a response to the client
        response = "Message received!"
        client_socket.send(response.encode())

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    server()
