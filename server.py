import socket
import threading

def handle_client(client_socket, client_address):
    print("Connected to client:", client_address)

    while True:
        # Receive and print the client's message
        message = client_socket.recv(1024).decode()
        if not message:
            break  # Exit the loop if no more messages

        print("Received message from client:", message)

        # Send a response back to the client
        response = "Server says: Hello, client!"
        client_socket.send(response.encode())

    # Close the client connection
    client_socket.close()
    print("Client connection closed:", client_address)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 5555)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print("Server listening on {}:{}".format(*server_address))

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
