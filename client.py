import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5004
client.connect((socket.gethostname(), port))
print(f"Connected to server at {socket.gethostname()}:{port}")

message_to_server = "Hello from the client!"
client.send(bytes(message_to_server, 'utf-8'))

data = client.recv(1024)
print("Received from server:", data.decode())

client.close()
