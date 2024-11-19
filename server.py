import socket

def server():
    """
    A simple server program that listens for connections from a client and sends commands to be executed remotely.

    The server:
    - Accepts a connection from the client.
    - Sends commands entered by the user to the client.
    - Receives and displays the execution result from the client.
    - Closes the connection when the 'exit' command is issued.
    """
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Listening for connections on {host}:{port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established!")

    while True:
        command = input("Shell> ")

        if command.lower() == 'exit':
            client_socket.send(b'exit')
            break
        client_socket.send(command.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    client_socket.close()

if __name__ == "__main__":
    server()
