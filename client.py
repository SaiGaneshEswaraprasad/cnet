import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=5004
s.connect(socket.gethostname(),port)
print("Connected")
z="hello from client"
z=str.encode(z,"utf-8")
s.send(z)
print(z.decode("utf-8"))