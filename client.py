import socket
import logging

# Config Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class TCPClient(object):
    def __init__(self, host='127.0.0.1', port=6000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            logging.info(f'Connected to {self.host}:{self.port}')
        except Exception as e:
            logging.error(f'Error connecting to {self.host}:{self.port}: {e}')
        
    def send_message(self, message):
        try:
            self.client_socket.send(message.encode('utf-8'))
            logging.info(f'Sent message: {message}')
            response = self.client_socket.recv(1024).decode('utf-8')
            logging.info(f'Received message: {response}')

            if message == 'DESCONEXION':
                self.client_socket.close()
                logging.info(f'Disconnected from {self.host}:{self.port}')
                return False
            return True

        except Exception as e:
            logging.error(f'Error sending message: {e}')
            self.client_socket.close()

    def disconnect(self):
        self.client_socket.close()
        logging.info(f'Disconnected from {self.host}:{self.port}')

if __name__ == '__main__':
    client = TCPClient()
    client.connect()

    while True:
        message = input('Ingrese un mensaje o escriba DESCONEXION para salir: ')
        if not client.send_message(message):
            break
