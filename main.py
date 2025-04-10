#importar a biblioteca random para fazer os sorteios aletórios de jogadores, dados e faces.(importei tambem a sleep por orientação
#dos meus colegas só para o jogo não ficar tão rápido

import random
from time import sleep

#criar a variavel para que o computador possa armazenar e contabilizar as quantidades de jogadores

quantidadeJogadores= 0


#criar as faces dos dados para serem sorteadas aleatóriamente por meio do random

daVerde = 'CPCTPC'
daAmarelo = 'TPCTPC'
daVermelho = 'TPTCPT'


#lista dos dados, 13 no total sendo 6 verdes, 4 amarelos e 3 vermelhos

dados = ['dVerde', 'dVerde', 'dAmarelo', 'dVermelho', 'dVerde', 'dVerde', 'dAmarelo', 'dVermelho', 'dVerde', 'dVerde', 'dAmarelo', 'dVermelho', 'dAmarelo']

#lista dos jogadores para o computador armazenar os nomes, assim possibilitando mostrar quando é a vez de cada um e contar os pontos

jogadores= []
#criando um dicionário para armazenar a quantidade de cerebro por jogador
placar = {}

#boas vindas ao jogo

print(' _____________________________________' )
print('|                                     |')
print('|     BEM VINDO AO ZOMBIE DICE!       |')
print('|                                     |')
print('|_____________________________________| \n')

#Quantidade de jogadores. pergunta ao usuário a quantidade de jogadores e impossibilita que tenha menos do que 2 por partida.

while quantidadeJogadores < 2:
    quantidadeJogadores = int(input('Insira a quantidade de jogadores: (ops: somente números) \n'))
    if quantidadeJogadores < 2:

        print('----------------- ERRO ---------------------\n')

        print('---Você precisa ter no mínimo 2 jogadores---\n')


#nome dos jogadores. Pergunta o nome de cada jogar e armazena na lista dos jogadores por meio do append.


for i in range (0,quantidadeJogadores):
    nome = input(f'Digite o nome do jogador {i} \n')
    jogadores.append(nome)
    # Iniciando o placar dos jogadores
    placar[nome] = 0

