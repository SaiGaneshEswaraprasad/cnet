import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5004
s.bind((socket.gethostname(), port))
s.listen(1)  # Allow only one connection

print("Waiting for a connection...")
c, adr = s.accept()
print(f"Connected to {adr} established")

while True:
    # Server sends a message
    message_to_send = input("Server: ")
    c.send(bytes(message_to_send, "utf-8"))

    # Server receives a message
    data = c.recv(1024)
    if not data:
        break
    print(f"Client: {data.decode()}")

# Close the connection
print(f"Connection with {adr} closed.")
c.close()
