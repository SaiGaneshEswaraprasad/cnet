import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=5004
client_socket.connect(('localhost', port))

filename = input("Enter the filename: ")
client_socket.sendall(filename.encode('utf-8'))

file_data = client_socket.recv(1024)

print(file_data.decode('utf-8'))

client_socket.close()