import socket
import time

HOST = "0.0.0.0"
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server berjalan di port {PORT} ...")

while True:
    conn, addr = server_socket.accept()
    print("Client terhubung:", addr)

    data = conn.recv(1024)
    print("Pesan diterima:", data.decode())

    # Delay 5 detik → untuk memicu timeout pada client
    time.sleep(5)

    conn.sendall(b"Balasan dari server")
    conn.close()
