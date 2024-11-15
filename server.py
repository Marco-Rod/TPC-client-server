import socket
import threading
import logging

# Config Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class TCPServer(object):
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        logging.info(f'Server started on port {self.port}')
        logging.info(f'Server listening on host {self.host}')

    def handle_client(self, client_socket, client_address):
        logging.info(f'Client connected from {client_address}')
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                logging.info(f'Received message: {message}, address: {client_address}')

                if message =='DESCONEXION':
                    logging.info(f'Client disconnected from {client_address}')
                    client_socket.send('Desconectando...'.encode('utf-8'))
                    break
                else:
                    response = f'{message.upper()}'
                    client_socket.send(message.encode('utf-8'))
                    logging.info(f'Sent message: {response}, address: {client_address}')
            except Exception as e:
                logging.error(f'Error handling client: {e}')
                break
        
        client_socket.close()
        logging.info(f'Client disconnected from {client_address}')

    def start(self):
        logging.info('Starting server...')
        try:
            while True:
                client_socker, client_address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socker, client_address))
                client_thread.start()
        except KeyboardInterrupt:
            logging.info('Server stopped')
        finally:
            self.server_socket.close()

if __name__ == '__main__':
    server = TCPServer()
    server.start()
