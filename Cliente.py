import socket
import os
#udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 6666


#while True:
   # mensagem = input()
   #tcp.send(str.encode(mensagem))

caminho_base = 'C:\\uridrive\\'

arquivos = os.listdir(caminho_base)

for arquivo in arquivos:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    destino = (host, port)
    tcp.connect(destino)
    caminho_absoluto = os.path.join(caminho_base, arquivo)
   # print(caminho_absoluto)
    arquivo_leitura = open(caminho_absoluto, 'rb')
    b = arquivo_leitura.read(1024)

    c = str.encode(arquivo + '#####')
    #tcp.send(str.encode(arquivo))
    print(c)
    tcp.send(c)
    tcp.send(b)
    tcp.close()


#mensagem = input()




