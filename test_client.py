import unittest
from client import TCPClient

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = TCPClient()
        self.client.connect()

    def test_send_message(self):
        # Enviar un mensaje al servidor
        self.client.send_message("Hola, servidor!")
    
    def test_disconnection(self):
        # Desconectar al servidor
        self.client.send_message("DESCONEXION")

    def tearDown(self):
        self.client.disconnect()


if __name__ == '__main__':
    unittest.main()
