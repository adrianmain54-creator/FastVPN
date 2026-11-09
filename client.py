import socket

class VPNClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send_data(self, data):
        self.client.send(data.encode())

    def receive_data(self):
        return self.client.recv(1024).decode()

    def close_connection(self):
        self.client.close()

if __name__ == '__main__':
    client = VPNClient('127.0.0.1', 55555)
    client.send_data('Hello, server!')
    print(client.receive_data())
    client.close_connection()