import socket
import threading

class VPN:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def handle_client(self, conn, addr):
        print(f'New Connection: {addr} connected.')
        conn.close()

    def start(self):
        print(f'Server started on {self.host}:{self.port}')
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

if __name__ == '__main__':
    vpn = VPN('127.0.0.1', 55555)
    vpn.start()