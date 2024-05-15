import socket

SERVER_ADDRESS = ('172.16.16.101', 45000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

while True:
    request = input("Masukkan perintah (TIME/QUIT): ").strip()
    client_socket.sendall(request.encode())

    if request == "QUIT":
        break

    response = client_socket.recv(1024).decode()
    print(response)

client_socket.close()