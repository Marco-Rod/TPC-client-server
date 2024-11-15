import unittest
import socket
import threading

from server import TCPServer


class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializar el servidor en un hilo separado
        cls.server = TCPServer()
        cls.server_thread = threading.Thread(target=cls.server.start)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    def test_server_connection(self):
        # Conectar al servidor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 5000))
        client_socket.send("Hola, servidor!".encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        self.assertIn("Hola, servidor!", response)
        client_socket.send('DESCONEXION'.encode('utf-8'))
        client_socket.close()
    
    @classmethod
    def tearDownClass(cls):
        # Desconectar al servidor al finalizar las pruebas
        cls.server.server_socket.close()


if __name__ == '__main__':
    unittest.main()
    