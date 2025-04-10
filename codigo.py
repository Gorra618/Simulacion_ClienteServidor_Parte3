import time
import random

class Node:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = []  # Buffer para almacenar mensajes

    def newConection(self, node):
        self.conexiones.append(node)
    
    def sendMsg(self, msg):
        print(f"{self.nombre} envia mensaje: {msg}")
        for nodo in self.conexiones:
            nodo.receiveMsg(msg)

    def receiveMsg(self, msg):
        # Simula la congestión añadiendo el mensaje al buffer
        print(f"{self.nombre} recibe mensaje: {msg} (almacenado en buffer)")
        self.buffer.append(msg)

    def procesar_buffer(self):
        print(f"{self.nombre} procesando buffer...")
        while self.buffer:
            # Simula la pérdida de paquetes con una probabilidad del 30%
            if random.random() < 0.3:
                msg_perdido = self.buffer.pop(0)
                print(f"{self.nombre} perdió el mensaje: {msg_perdido}")
            else:
                msg_procesado = self.buffer.pop(0)
                print(f"{self.nombre} procesó el mensaje: {msg_procesado}")

    def remove(self, node):
        if node in self.conexiones:
            self.conexiones.remove(node)
            print(f"Conexion eliminada con {node.nombre}")
    
    
server = Node("Servidor")
client1 = Node("Cliente_1")
client2 = Node("Cliente_2")
client3 = Node("Cliente_3")

print("Conectando")
time.sleep(2)
server.newConection(client1)
server.newConection(client2)
server.newConection(client3)

print("Eliminando usuarios")
time.sleep(2)
server.remove(client2)

print("Reconectando")
time.sleep(2)
server.newConection(client1)
server.newConection(client2)

server.sendMsg("Hola de nuevo a todos los clientes conectados")

# Procesar buffers de los clientes
time.sleep(2)
client1.procesar_buffer()
client2.procesar_buffer()
client3.procesar_buffer()