import socket
import threading

HOST = '0.0.0.0'
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server berjalan di port {PORT} ...")

clients = []  # list untuk menyimpan semua koneksi client


# kirim pesan ke semua client lain
def broadcast(message, source_client):
    for client in clients:
        if client != source_client:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


# menangani client
def handle_client(client_socket, addr):
    print(f"Client terhubung: {addr}")
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break

            print(f"Dari {addr}: {message.decode()}")
            broadcast(message, client_socket)

    except:
        pass

    print(f"Client terputus: {addr}")
    clients.remove(client_socket)
    client_socket.close()


# menerima koneksi baru
def receive_connections():
    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()


receive_connections()
