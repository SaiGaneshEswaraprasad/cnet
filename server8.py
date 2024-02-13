import socket
import threading
import os

def handle_client(client_socket, addr):
    try:
        # Receive file name from client
        file_name = client_socket.recv(1024).decode()

        # Check if the file exists
        if os.path.exists(file_name):
            # Open and send the file in chunks
            with open(file_name, 'rb') as file:
                data = file.read(1024)
                while data:
                    client_socket.sendto(data, addr)
                    data = file.read(1024)
        else:
            # Send an error message if the file doesn't exist
            client_socket.sendto(b'File not found', addr)
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port=5004
    server_socket.bind(('localhost', port))

    print(f"Server listening on port {port}...")

    try:
        while True:
            client_data, client_addr = server_socket.recvfrom(1024)
            client_thread = threading.Thread(target=handle_client, args=(server_socket, client_addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        server_socket.close()

if __name__ == "__main__":
    main()
