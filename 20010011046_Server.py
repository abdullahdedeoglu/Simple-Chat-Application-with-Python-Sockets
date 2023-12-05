import socket
import threading

clients = {}

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()

print('Sunucu dinlemede...')


def broadcast(message, sender):
    for client_socket in clients:
        if client_socket != sender:
            client_socket.send(message.encode())


def handle_client(client_socket, addr):
    client_socket.send('Kullanıcı adınızı girin:'.encode())
    username = client_socket.recv(1024).decode()

    if username in clients.values():
        client_socket.send(
            'Bu kullanıcı adı zaten kullanılıyor. Başka bir kullanıcı adı seçin.'.encode())
        client_socket.close()
        return

    clients[client_socket] = username
    broadcast(f'{username} sohbet odasına katıldı.', client_socket)

    client_socket.send(
        f'Hoş geldiniz, {username}! Sohbete başlayabilirsiniz.'.encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()

            broadcast(f'{username}: {message}', client_socket)
        except:
            client_socket.close()
            del clients[client_socket]
            broadcast(f'{username} sohbet odasından ayrıldı.', client_socket)
            break


while True:
    client_socket, addr = server_socket.accept()
    print('Bağlantı alındı:', addr)

    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, addr))
    client_thread.start()
