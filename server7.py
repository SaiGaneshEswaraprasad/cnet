import socket
import threading
import os

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    # Receive the client's file choice
    file_choice = client_socket.recv(1024).decode()
    print(f"Client {client_address} chose file: {file_choice}")

    # Check if the requested file exists
    file_path = os.path.join("server_files", file_choice)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        # Send the file to the client
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
        print(f"File '{file_choice}' sent to {client_address}")
    else:
        # Inform the client that the file does not exist
        client_socket.send(b"File not found")

    # Close the connection with the client
    client_socket.close()
    print(f"Connection with {client_address} closed")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 5004
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()