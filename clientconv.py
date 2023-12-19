import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5004
s.connect((socket.gethostname(), port))

while True:
    # Client receives a message
    data = s.recv(1024)
    if not data:
        break
    print(f"Server: {data.decode()}")

    # Client sends a message
    message_to_send = input("Client: ")
    s.send(bytes(message_to_send, "utf-8"))

# Close the connection
s.close()
