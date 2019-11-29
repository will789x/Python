import threading
import time
import random
#
x = int(input('Informe o numero de Taxistas disponiveis'))
z = int(input('Informe o numero de Moto_Taxistas disponiveis'))
y = int(input('Informe o numero maximo de Passageiros '))

taxistas = []
passageiros = []

moto_taxistas = []
moto_passageiros = []
condicao = threading.Condition()
moto_condicao = threading.Condition()

def Fazer_Corrida():
    nome = threading.current_thread().name

    while True:
        print('Taxista %s pronto para serviço' % nome)
        condicao.acquire()
        while not len(passageiros):
            print('Nenhum passageiro aguardando, Taxista %s foi dormir...' % nome)
            condicao.wait()
            print('Taxista %s foi acordado...' % nome)
        valor = passageiros.pop()
        condicao.release()
        print('Taxista %s em serviço' % nome)
        time.sleep(random.randint(10, 20))
    print('Taxista %s encerrando serviço' % nome)

def Fazer_Moto_Corrida():
    nome = threading.current_thread().name
    while True:
        print('Moto-Taxista %s pronto para serviço' % nome)
        moto_condicao.acquire()
        # print('Consumidor adquiriu lock')
        while not len(moto_passageiros):
            print('Nenhum passageiro aguardando, Moto-Taxista %s foi dormir...' % nome)
            moto_condicao.wait()
            print('Moto-Taxista %s foi acordado...' % nome)
        valor = moto_passageiros.pop()
        moto_condicao.release()
        print('Moto-Taxista %s em serviço' % nome)
        time.sleep(random.randint(10, 20))
    print('Moto-Taxista %s encerrando serviço' % nome)


def Solicitar_Corrida():
    nome = threading.current_thread().name
    print('Passageiro %s chegou ao ponto de taxi' % nome)
    if (len(passageiros) + len(moto_passageiros) > y):
        print('passageiro %s se assustou com o tamanho da fila e foi embora'  % nome)
        return
    condicao.acquire()
    passageiros.append(threading.current_thread())

    print('Passageiro %s  acordou o taxista ' % nome)
    condicao.notify()
    condicao.release()

def Solicitar_Moto_Corrida():
    nome = threading.current_thread().name
    print('moto-Passageiro %s chegou ao ponto de taxi' % nome)
    if (len(passageiros) + len(moto_passageiros) > y):
        print('moto-Passageiro %s se assustou com o tamanho da fila e foi embora'  % nome)
        return
    moto_condicao.acquire()
    moto_passageiros.append(threading.current_thread())

    print('moto-Passageiro %s  acordou o moto-taxista ' % nome)
    moto_condicao.notify()
    moto_condicao.release()



for i in range(x):
    t = threading.Thread(target=Fazer_Corrida, name=str(i))
    taxistas.append(t)

for taxista in taxistas:
    taxista.start()

for i in range(z):
    t = threading.Thread(target=Fazer_Moto_Corrida, name=str(i))
    moto_taxistas.append(t)

for moto_taxista in moto_taxistas:
    moto_taxista.start()


while True:
    opcao = random.randint(0, 1)
    if opcao == 0:
        t2 = threading.Thread(target=Solicitar_Corrida)
        t2.start()
    else:
        t2 = threading.Thread(target=Solicitar_Moto_Corrida)
        t2.start()

    time.sleep(random.randint(0, 2))
