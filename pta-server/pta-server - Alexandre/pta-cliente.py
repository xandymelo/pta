from socket import socket, AF_INET, SOCK_STREAM

#serverName = '127.0.0.1'
serverName = '127.0.0.1'
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_STREAM)

#Conecta ao servidor
clientSocket.connect((serverName,serverPort))

#Recebe mensagem do usuario e envia ao servidor
message = input('Digite um comando: ')
clientSocket.send(message.encode('ascii'))

#Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
print("Retorno do Servidor:",modifiedMessage.decode())

if modifiedMessage.decode() == 'OK':
    message = input('Digite seu usuario: ')
    clientSocket.send(message.encode('ascii'))


clientSocket.close()