import socket
s = socket. socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5003
s. bind((socket.gethostname(), port))
s. listen(100)
while True:
        c, adr =s. accept()
        print(f"Connected to {adr} established")
        c.send(bytes("He110 from server", "utf-8"))
        data =c. recv(1024)
        print("received from client: ", data.decode())
        c. close()