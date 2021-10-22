from Conv import conv
import socket

def padrao():
    
    unidade1 = clientsocket.recv(1024)
    unidade2 = clientsocket.recv(1024)
    valor = clientsocket.recv(1024)
    conv1 = conv(unidade1.decode('utf-8'), unidade2.decode('utf-8'), valor.decode('utf-8'))

    valor_conv, valor_tipo = conv1.conv()
    valor_conv = str(valor_conv)
    clientsocket.send(valor_conv.encode('utf-8'))
    clientsocket.send(valor_tipo.encode('utf-8'))
    continuar = clientsocket.recv(1024)

    if continuar.decode('utf-8') == 1 or continuar.decode('utf-8') == str(1):
        print("Nova operação do cliente \"{}\"".format(str(addr)))
        padrao()
    elif continuar.decode('utf-8') == 2 or continuar.decode('utf-8') == str(2):
        print("Fim das operações com o cliente \"{}\".".format(str(addr)))
        clientsocket.close()
    else:
        pass

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12000

serversocket.bind((host, port))

serversocket.listen()
print("Server listening on port {}.\n".format(port))

while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from {}".format(str(addr)))

    padrao()