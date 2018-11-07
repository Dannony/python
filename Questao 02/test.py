from socket import*
import struct
import loja
import Pacote
import threading

print('Reunindo Informações da Lista de Produtos...')
lista = loja.lista_produto()
#campos = lista.split(',')
for i in range(len(lista)):
    produto = lista[i][0]
    prel1 = lista[i][1]
    prel2 = lista[i][2]

    produtos = ('resposta',1.0,2.0)
    print(produto)
    print(prel1)
    print(prel2)
