import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 55))
server_socket.listen(1)
print("Server listening on port 55...")

while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        filename = client_socket.recv(1024).decode('utf-8')
        print(f"Client requested file: {filename}")

        try:
            with open(filename, 'rb') as file:
                file_data = file.read()
                client_socket.sendall(file_data)
        except FileNotFoundError:
            client_socket.sendall(b"File not found")

        client_socket.close()
        print(f"Connection with {client_address} closed")