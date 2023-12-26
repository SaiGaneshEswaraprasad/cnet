import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5004
s.bind((socket.gethostname(), port))
s.listen(10)

print("Waiting for a connection...")
c, adr = s.accept()
print(f"Connected to {adr} established")

while True:
    message_to_send = input("Server: ")
    c.send(bytes(message_to_send, "utf-8"))

    if message_to_send.lower() == "bye":
        print(f"Connection with {adr} closed.")
        break

    data = c.recv(1024)
    if not data:
        break
    print(f"Client: {data.decode()}")

print(f"Connection with {adr} closed.")
c.close()
