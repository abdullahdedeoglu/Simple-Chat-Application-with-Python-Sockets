# Simple-Chat-Application-with-Python-Sockets
This project consists of a simple chat application implemented in Python using the socket library for establishing communication between a server and multiple clients.
Server-side:
Server Code: 20010011046_server.py

The server.py file contains the server-side code for handling multiple client connections.
The server listens on a specified IP address ('127.0.0.1') and port (12345) for incoming connections.
It handles multiple clients simultaneously by creating threads for each client connection.
The server receives messages from clients and broadcasts them to all other connected clients.
Client-side:
Client Code: 20010011046_client.py

The client.py file contains the client-side code for connecting to the server.
Each client connects to the server using the server's IP address ('127.0.0.1') and port (12345).
Clients can send messages to the server, and the server broadcasts these messages to all other connected clients.
It uses multi-threading to handle sending and receiving messages simultaneously.
# How to Use:
Server Setup:

Run the server.py file to start the chat server.
The server will listen for incoming connections on the specified IP address and port.
Client Connection:

Run the client.py file to connect to the server as a client.
Enter a username when prompted to join the chat room.
Start sending and receiving messages within the chat room.
# Features:
Server:

Listens for incoming connections on a specified IP address and port.
Handles multiple client connections concurrently using multi-threading.
Broadcasts messages received from one client to all other connected clients.
Client:

Connects to the server using the server's IP address and port.
Provides a username to enter the chat room.
Sends messages to the server and receives messages broadcasted by the server.
# Dependencies:
Python 3.x
socket library
threading module
# How to Run:
Server:

Run server.py on a system to start the server.
Client:

Run client.py on multiple systems to connect as clients and join the chat room.
# Notes:
Ensure that the server is running before clients attempt to connect.
The server handles connections from multiple clients and manages the message broadcasting among them.
# Files Included:
20010011046_server.py: Server-side code for handling client connections and message broadcasting.
20010011046_client.py: Client-side code for connecting to the server, sending messages, and receiving broadcasted messages.
README.md: Documentation file explaining the functionalities, setup, and usage of the chat application.
# Author:
Abdullah Dedeoglu
