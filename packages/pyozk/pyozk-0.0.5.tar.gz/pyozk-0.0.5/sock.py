# import socket

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Get the hostname
# host = socket.gethostname()
# port = 12345  # Choose a port number

# # Bind to the port
# server_socket.bind((host, port))

# # Listen for incoming connections
# server_socket.listen(5)

# print('Server listening on {}:{}'.format(host, port))

# while True:
#     # Establish connection with client
#     client_socket, addr = server_socket.accept()

#     print('Got connection from', addr)

#     # Send data to the client
#     client_socket.sendall(b'Thank you for connecting')

#     # Receive data from the client
#     data = client_socket.recv(1024)
#     print('Received:', data.decode())

#     # Close the connection
#     client_socket.close()
