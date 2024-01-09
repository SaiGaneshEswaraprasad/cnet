import socket

def request_file_from_server(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 57
    client_socket.connect((host, port))

    # Send the requested file name to the server
    client_socket.send(file_name.encode())

    # Receive the file content from the server
    received_data = client_socket.recv(1024)
    while received_data:
        print(received_data.decode(), end="")
        received_data = client_socket.recv(1024)

    # Close the connection with the server
    client_socket.close()

if _name_ == "_main_":
    requested_file = input("Enter the name of the file you want to request: ")
    request_file_from_server(requested_file)