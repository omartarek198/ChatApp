import socket
import threading

# Dictionary to store client public keys
client_public_keys = {}

client_sessions= []
def handle_client(client_socket, client_address):
    print("Connected to client:", client_address)

    # Receive the client's public key
    try:
        public_key = client_socket.recv(1024).decode()
        if not public_key:
            raise ConnectionResetError
        client_socket.send("ok".encode())
    except ConnectionResetError:
        print("No public key received from client:", client_address)
        client_socket.close()
        # Delete the key for the client from client_public_keys
        client_port = client_address[1]
        if client_port in client_public_keys:
            del client_public_keys[client_port]
        return

    # Save the public key in the dictionary with the client's port as the key
    client_port = client_address[1]
    client_public_keys[client_port] = public_key
    print("Received public key from client {}:{} :-{}-".format(*client_address, public_key))

    while True:
        # Receive and print the client's message
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break  # Exit the loop if no more messages
            print("Received message from client:", message)

            if message == "Get_Keys":
                # Send the keys of all clients as a response back to the client
                keys = "\n".join(client_public_keys.values())
                client_socket.send(keys.encode())
            else:
                # Send a default response back to the client
                for i in client_sessions:
                    if i[0] != client_address:
                        i[1].send(message.encode())
                          
                    response = "Server says: delivered!"
                    client_socket.send(response.encode())
        except ConnectionResetError:
            client_port = client_address[1]
            if client_port in client_public_keys:
                del client_public_keys[client_port]
        
                break

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
    client_sessions.append((client_address,client_socket))
    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
