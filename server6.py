import socket
import os

def serve_client(client_socket):
    # Assume binary_file.bin is the binary file you want to send
    filename = 'binary_file.bin'
    file_size = os.path.getsize(filename)

    # Send the file size to the client
    client_socket.send(str(file_size).encode())

    # Open the binary file and send its content
    with open(filename, 'rb') as file:
        file_content = file.read()
        client_socket.sendall(file_content)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 56))
    server_socket.listen(10)  # Listen for one incoming connection at a time

    print("Server listening on port 56")

    while True:
        # Wait for a connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Serve the client and then close the connection
        serve_client(client_socket)
        client_socket.close()

if __name__ == "__main__":
    main()