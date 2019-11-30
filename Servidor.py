import socket
import os

#udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(tcp)

ip = socket.gethostbyname('www.google.com')
print(ip)

porta = 80

#tcp.connect((ip, porta))


print ('conectado ao servidor do google no ip', ip)

r = 'GET / HTTP/1.1\nHOST: www.google.com.br\n\n'
request = str.encode(r)
#tcp.send(request)

#while True:
 #   dados = tcp.recv(1024)
 #   if len(dados) < 1:
 #       break
 #   else:
 #       print(dados)
#tcp.close()

HOST = ''
PORT = 6666
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (HOST, PORT)
tcp.bind(origem)

tcp.listen(5)
while True:
    con, cliente = tcp.accept()
    print("Cliente %s conectado" % str(cliente))

    nomearq = ''

    mensagem = con.recv(1024)
    mensagem = mensagem.decode("UTF-8")
    print(mensagem)

    if mensagem.find('#####') >= 0:
        nomearq = mensagem[:mensagem.find('#####')]
        print(nomearq)

    msg = mensagem[mensagem.find('#####') + 5:]
    print(msg)

    arquivo = open('C:\\tmp\\'+ nomearq, 'w')

    mensagem = con.recv(1024)
    mensagem = mensagem.decode("UTF-8")

    texto = str(msg)
    arquivo.write(texto)
    arquivo.close()

    #print("Cliente %s enviou a mensagem: %s " % (str(cliente), mensagem))
    #print("Finalizando conexao")