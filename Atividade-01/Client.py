# python -u "c:\Users\User\Documents\Programinhas\vscode\Python\IF_Exercises\SOR\Atividade-01\Client.py"
import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12000

clientsocket.connect((host, port))

while True:

    print("|\n+{:30}-{:35}+\n|{:^65} |\n+{:30}-{:35}+\n|{:<30}|{:35s}|\n+{:30}+{:35}+\n|{:30s}|{:<35}|\n|{:30s}|{:<35}|\n|{:<30}|{:35}|\n+{:30}+{:35}+".format(
    "—"*30 , "—"*35
    , "Conversor de velocidade "
    , "—"*30 , "—"*35
    , " Unidades disponíveis: " , "■"*35
    , "—"*30 , "—"*35
    , "■"*30 , " 1: Km/h."
    , "■"*30 , " 2: m/s."
    , "■"*30 , " 3: mi/h."
    , "—"*30 , "—"*35))

    unidade1 = input("| Diga a unidade inicial: ")
    unidade2 = input("| Diga a unidade final: ")
    valor = input("| Diga o valor: ")
    
    
    clientsocket.send(unidade1.encode('utf-8'))
    clientsocket.send(unidade2.encode('utf-8'))
    clientsocket.send(valor.encode('utf-8'))
    valor_conv = clientsocket.recv(1024)
    valor_tipo = clientsocket.recv(1024)
    
    print("| Seu valor convertido é igual a: \"{} {} \"!".format(valor_conv.decode('utf-8'), valor_tipo.decode('utf-8')))

    continuar = input("|")
    continuar = input("|\n+{:30}+{:35}+\n|{:<30}|{:35s}|\n+{:30}+{:35}+\n|{:30s}|{:<35}|\n|{:<30}|{:35}|\n+{:30}+{:35}+\n| ".format(
    "—"*30 , "—"*35
    , " Deseja fazer outra conversão?" , "■"*35
    , "—"*30 , "—"*35
    , "■"*30 , " 1: Sim"
    , "■"*30 , " 2: Não"
    , "—"*30 , "—"*35))

    if continuar == 1 or continuar == str(1):
        clientsocket.send(continuar.encode('utf-8'))
        continue
    elif continuar == 2 or continuar == str(2):
        clientsocket.send(continuar.encode('utf-8'))
        break
    else:
        pass
