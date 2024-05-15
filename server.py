import socket
import threading
import time

class TimeServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 45000))
        self.server_socket.listen(5)

    def run(self):
        print("Server sudah berjalan di port 45000")
        while True:
            conn, addr = self.server_socket.accept()
            client_thread = ClientThread(conn, addr)
            client_thread.start()

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            request = data.decode().strip()
            if request == "TIME":
                response = f"JAM{time.strftime('%I:%M:%S %p'):<13}"
            elif request == "QUIT":
                response = "QUIT"
                self.conn.sendall(response.encode())
                self.conn.close()
                break
            else:
                response = "Perintah tidak valid"
            self.conn.sendall(response.encode())

if __name__ == "__main__":
    server = TimeServer()
    server.start()