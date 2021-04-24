from socket import *

serverPort = 11500
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("CUMP")

verify_client = False
aux = 0.

while 1:
    try:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode() #converter para string novamente
        #VERIFICAR SE A PRIMEIRA MENSAGEM É 'CUMP'
        if sentence != "CUMP" and aux == 0:
            capitalizedSentence = 'NOK'
        else:
            capitalizedSentence = 'OK'
        #VERIFICAÇÃO DE USUÁRIO
        if aux == 1:
            aux2 = 0
            arquivo = open('users.txt','r')
            for lines in arquivo:
                if lines == sentence:
                    aux2 = 1
            if aux2 == 0:
                capitalizedSentence = 'NOK'
            else:
                capitalizedSentence = 'OK'
        aux += 1
        connectionSocket.send(capitalizedSentence.encode('ascii'))

            





        connectionSocket.close()
    except (KeyboardInterrupt, SystemExit):
        break

serverSocket.shutdown(SHUT_RDWR)
serverSocket.close()