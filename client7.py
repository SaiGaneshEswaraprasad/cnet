import socket

def request_file_from_server(file_choice, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    server_port = 5004
    client_socket.connect((host, server_port))

    # Send the chosen file to the server
    client_socket.send(file_choice.encode())

    # Print the port number of the client
    print(f"Connected to server on port {port}")

    # Receive the file content from the server
    received_data = client_socket.recv(1024)
    while received_data:
        print(received_data.decode(), end="")
        received_data = client_socket.recv(1024)
    print(received_data)

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    # Get the client's port number
    client_port = int(input("Enter your port number: "))

    # Get the file choice from the client
    file_choice = input("Enter the name of the file you want to request : ")

    # Run the client with the chosen port number and file choice
    request_file_from_server(file_choice, client_port)