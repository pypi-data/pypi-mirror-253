import socket
import json 


class SenderNetwork:

    def __init__(self, ip, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((ip, port))
        self.server.listen(0)

    def send(self, connection, data):
        json_data = json.dumps(data)
        connection.sendall(json_data.encode())


class ReceiverNetwork:

    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
    
    def receive(self):
        json_data = b''
        while True:
            try:
                json_data = json_data + self.connection.recv(3024)
                return json.loads(json_data)
            except:
                continue
