from socket import *
from os import listdir,chdir,open
from os.path import isfile, join

serverPort = 11500
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("CUMP")
aux = float("inf")
verify_client = False
apresentacao = True

while 1:
    try:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode() #converter para string novamente
        #VERIFICAR SE A PRIMEIRA MENSAGEM É 'CUMP'
        sentence = sentence.split(" ")
        if aux == float("inf"):
            aux = sentence[0]
        else:
            aux = int(aux) + 1
        if apresentacao == True and sentence[1] != "CUMP":
            capitalizedSentence = '{} NOK'.format(aux)
            connectionSocket.send(capitalizedSentence.encode('ascii'))
            break
        capitalizedSentence = '{} NOK'.format(aux)
        if sentence[1] == "CUMP":
            try:
                arquivo = open('users.txt','r')
                for lines in arquivo:
                    lines2 = lines.rstrip() #retirar o /n
                    if  lines2 == sentence[2]:
                        capitalizedSentence = '{} OK'.format(aux)
                verify_client = True
            except:
                pass
        elif sentence[1] == 'TERM':
            capitalizedSentence = '{} OK'.format(aux)
            verify_client = True
        elif sentence[1] == 'LIST':
            try:
                path = r"C:\Users\Alexandre\Documents\GitHub\pta\pta-server\files"
                files = [f for f in listdir(path) if isfile(join(path, f))]
                leng = len(files)
                capitalizedSentence = "ARQS {}".format(leng)
                separator = ','
                result = [separator.join(files)]
                result2 = "{} {}{}".format(capitalizedSentence,result[0],".")
                capitalizedSentence = result2
            except:
                pass
        elif sentence[1] == 'PEGA':
            path = r"\Users\Alexandre\Documents\GitHub\pta\pta-server\files"
            chdir(path)
            try:
                arq = open(sentence[1],"r")

            except:
                continue

        apresentacao = False
        connectionSocket.send(capitalizedSentence.encode('ascii'))    
        if verify_client == True:    
            break

        
    except (KeyboardInterrupt, SystemExit):
        break

serverSocket.shutdown(SHUT_RDWR)
serverSocket.close()