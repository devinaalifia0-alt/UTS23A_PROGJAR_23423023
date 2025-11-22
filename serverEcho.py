import socket

HOST = '0.0.0.0'   # listen ke semua interface
PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server berjalan di port {PORT} ...")
print("Menunggu koneksi ...")

conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    print("Pesan dari client:", data.decode())

    # kirim kembali (echo)
    conn.sendall(data)

conn.close()
server_socket.close()
