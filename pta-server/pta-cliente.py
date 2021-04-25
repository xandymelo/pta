from socket import socket, AF_INET, SOCK_STREAM

def retornoservidor():
    #Aguarda mensagem de retorno e a imprime
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    print("Retorno do Servidor:",modifiedMessage.decode())
    return modifiedMessage


#serverName = '127.0.0.1'
serverName = '127.0.0.1'
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_STREAM)

#Conecta ao servidor
clientSocket.connect((serverName,serverPort))


#Recebe mensagem do usuario e envia ao servidor
message = input('Digite um comando: ')
clientSocket.send(message.encode('ascii'))
modifiedMessage = retornoservidor()
modifiedMessage = modifiedMessage.decode()

if modifiedMessage[2:] == 'OK':
    message = input('Digite um comando: ')
    clientSocket.send(message.encode('ascii'))
    modifiedMessage = retornoservidor()
    modifiedMessage = modifiedMessage.decode()

clientSocket.close()

