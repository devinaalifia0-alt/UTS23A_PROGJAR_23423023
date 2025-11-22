import socket

HOST = "127.0.0.1"
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ---- Timeout saat connect (3 detik) ----
client_socket.settimeout(3)

try:
    client_socket.connect((HOST, PORT))
    print("Terhubung ke server!")

except socket.timeout:
    print("Koneksi timeout!")
    exit()

except Exception as e:
    print("Error:", e)
    exit()

# ---- Timeout saat membaca data (2 detik) ----
client_socket.settimeout(2)

try:
    client_socket.sendall(b"Tes Timeout")

    data = client_socket.recv(1024)
    print("Balasan server:", data.decode())

except socket.timeout:
    print("Koneksi timeout!")

except Exception as e:
    print("Error:", e)

client_socket.close()
