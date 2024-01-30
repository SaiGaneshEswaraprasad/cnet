import socket

def receive_file(client_socket):
    # Receive the file size from the server
    file_size = int(client_socket.recv(1024).decode())

    # Receive the file content
    file_content = client_socket.recv(file_size)

    # Assume received_file.bin is the file where you want to save the received content
    with open('received_file.bin', 'wb') as file:
        file.write(file_content)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 56))  # Connect to localhost on port 56

    # Request and receive file from the server
    receive_file(client_socket)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()