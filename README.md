Servidor y Cliente TCP
======================

Servidor TCP
------------
El servidor escucha en el puerto 6000 y espera conexiones de clientes. Cuando recibe una conexión espera que el cliente envie un mensaje. Si el cliente envia el mensaje DESCONEXION, se desconecta del servidor. En caso contrario, el servidor envia el mensaje original al cliente en mayúsculas.

Como ejecutar el servidor:

```bash
python server.py
```
Cliente TCP
-----------
El cliente se conecta al servidor TCP en el puerto 6000.

Ejecutar el cliente:

```bash
python client.py
```

Para enviar un mensaje al servidor, escriba el mensaje en la consola y presione enter. Para enviar el mensaje DESCONEXION, escriba DESCONEXION y presione enter.



Pruebas
-------
Para ejecutar las pruebas, ejecutar los siguientes comandos en la terminal:

```bash
python test_server.py
python test_client.py
```
en el caso de test_client.py, se espera que el servidor este siendo ejecutado para recibir los mensajes enviados por el cliente.