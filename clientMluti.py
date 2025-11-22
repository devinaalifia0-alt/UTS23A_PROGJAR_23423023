import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Terhubung ke server. Mulai chat ...")


# menerima pesan broadcast dari server
def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print("\nPesan baru:", msg)
        except:
            print("Koneksi terputus dari server.")
            client_socket.close()
            break


# thread untuk menerima pesan
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()


# kirim pesan secara manual
while True:
    pesan = input("")
    client_socket.send(pesan.encode())
