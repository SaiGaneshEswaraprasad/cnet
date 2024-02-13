import socket

def main():
    server_address = ('localhost', 59)

    file_name = input("Enter the file name to request: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Send file name to the server
        client_socket.sendto(file_name.encode(), server_address)

        # Receive and save the file
        with open(f'downloaded_{file_name}', 'wb') as file:
            while True:
                data, _ = client_socket.recvfrom(1024)
                if not data:
                    break
                file.write(data)

        print(f"File '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
