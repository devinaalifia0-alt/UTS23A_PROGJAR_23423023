import socket

HOST = '127.0.0.1'   # IP server
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# kirim pesan
pesan = "Tes Koneksi"
client_socket.sendall(pesan.encode())

# menerima balikan
data = client_socket.recv(1024)

print("Balasan dari server:", data.decode())

client_socket.close()
