from socket import *
from os import listdir,chdir,path
from os.path import isfile, join,dirname,abspath
from pathlib import Path

def cump(user,aux):
    arquivo = open('users.txt',"r")
    capitalizedSentence = '{} NOK'.format(aux)
    for lines in arquivo:
        lines2 = lines.rstrip() #retirar o /n
        if  lines2 == user:
            capitalizedSentence = '{} OK'.format(aux)
    arquivo.close()
    return capitalizedSentence
def enviar(capitalizedSentence):
    connectionSocket.send(capitalizedSentence.encode('ascii'))
def receber():
    sentence = connectionSocket.recv(1024).decode() #esperar por receber nova mensagem #converter para string novamente
    sentence = sentence.split(" ")
    return sentence



serverPort = 11500
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("CUMP")
aux = float("inf")
apresentacao = True

while 1:
    try:
        connectionSocket, addr = serverSocket.accept() #esperar por novas conexões
        sentence = receber()
        #--tratamento da contagem de mensagens
        #--começo

        if aux == float("inf"):
            aux = sentence[0]
        else:
            aux = int(aux) + 1
        #--fim

        #--tratamento para apresentação
        #--inicio
        if apresentacao == True:
            if sentence[1] != "CUMP":
                capitalizedSentence = '{} NOK'.format(aux)
                aux = float("inf")
            elif sentence[1] == "CUMP":
                capitalizedSentence = cump(sentence[2],aux)
            connectionSocket.send(capitalizedSentence.encode('ascii'))
            if capitalizedSentence[2:] == 'OK':
                apresentacao = False
                sentence = receber()
                aux = int(aux) + 1
            else:
                aux = float("inf")
        #--fim

        #--inicio do tratamento depois da confirmação do usuario
        if apresentacao == False:  
            aux2 = True
            while aux2 == True:
                capitalizedSentence = '{} NOK'.format(aux)
                if sentence[1] == 'TERM':
                    capitalizedSentence = '{} OK'.format(aux)
                    enviar(capitalizedSentence)
                    aux = float("inf")
                    aux2 = False
                elif sentence[1] == 'LIST':
                    try:
                        path = r"C:\Users\Alexandre\Documents\GitHub\pta\files"
                        files = [f for f in listdir(path) if isfile(join(path, f))]
                        leng = len(files)
                        capitalizedSentence = "ARQS {}".format(leng)
                        separator = ','
                        result = [separator.join(files)]
                        result2 = "{} {} {}".format(aux,capitalizedSentence,result[0])
                        capitalizedSentence = result2
                    except:
                        aux2 = False
                    enviar(capitalizedSentence)
                    aux = int(aux) + 1
                elif sentence[1] == 'PEGA':
                    try:
                       byte = os.stat_result(sentence[2]).st_size


                    except:
                        aux2 = False
                
                if aux2 == True:
                    sentence = receber()


        if apresentacao == True:
            connectionSocket.close()

        
    except (KeyboardInterrupt, SystemExit):
        break

serverSocket.shutdown(SHUT_RDWR)
serverSocket.close()