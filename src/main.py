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

    ''' 
    vamos começar os turnos e os sorteios dos dados, faces e jogadores.
    As pontuações e jogadas precisam ser contabilizadas e armazenadas.
    Os jogadores precisam escolher se querem continuar jogando os dados ou se passam a vez.
    '''

    # mandar o computador sortear um dos jogadores para começar o turno

    jogador = random.choice(jogadores)

    '''vamos pedir para o computador escolher aleatóriamente uma cor de dado e uma face desse dado escolhido, 
    em seguida ele contabiliza quantos passos, tiros e cerebros foram tirados,
    depois mostra o resultado.
    '''

    # primeiro dado
    rodada = False
    total_cerebros = []
    while rodada == False:

        for jogador in jogadores:
            turno = False

            # criando uma lista que contabiliza os posntos por jogador
            cerebrojogador = []
            tirojogador = []
            passojogador = []

            # função que reseta o copo e coloca todos os dados retirados novamente depois de cada partida
            while not turno:
                def resetarcopo():
                    dados = ['dVerde', 'dVerde', 'dAmarelo', 'dVermelho', 'dVerde', 'dVerde', 'dAmarelo', 'dVermelho',
                             'dVerde',
                             'dVerde', 'dAmarelo', 'dVermelho', 'dAmarelo']
                    return dados


                dados = resetarcopo()

                # variaveis de tiros, cerebros e passos para poder contabilizar, iniciando sempre em 0
                cerebros = 0
                passos = 0
                tiros = 0

                # indica a vez de qual jogador é
                print('---------------------------', jogador, 'é a sua vez---------------------------')
                sleep(1)

                # sorteia o primeiro dado e logo depois retira ele do copo
                dado1 = random.choice(dados)
                dados.remove(dado1)
                sleep(1)

                # variáveis que mostram qual em dado e face cair a ação que deve ser realizada
                if dado1 == 'dVerde':
                    face1 = random.choice(daVerde)
                    print('O primeiro dado é verde e você tirou um', face1)
                    if face1 == 'C':
                        cerebros = cerebros + 1
                    elif face1 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                elif dado1 == 'dVermelho':
                    face1 = random.choice(daVermelho)
                    print('O primeiro dado é Vermelho e você tirou um', face1)
                    if face1 == 'C':
                        cerebros = cerebros + 1
                    elif face1 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                else:
                    face1 = random.choice(daAmarelo)
                    print('O primeiro dado é Amarelo e você tirou um', face1)
                    if face1 == 'C':
                        cerebros = cerebros + 1
                    elif face1 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                # segundo dado

                dado2 = random.choice(dados)
                dados.remove(dado2)

                if dado2 == 'dVerde':
                    face2 = random.choice(daVerde)
                    print('O segundo dado é verde e você tirou um', face2)
                    if face2 == 'C':
                        cerebros = cerebros + 1
                    elif face2 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                elif dado2 == 'dVermelho':
                    face2 = random.choice(daVermelho)
                    print('O segundo dado é Vermelho e você tirou um', face2)
                    if face2 == 'C':
                        cerebros = cerebros + 1
                    elif face2 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                else:
                    face2 = random.choice(daAmarelo)
                    print('O segundo dado é Amarelo e você tirou um', face2)
                    if face2 == 'C':
                        cerebros = cerebros + 1
                    elif face2 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                # terceiro dado

                dado3 = random.choice(dados)
                dados.remove(dado3)

                if dado3 == 'dVerde':
                    face3 = random.choice(daVerde)
                    print('O terceiro dado é verde e você tirou um', face3, '\n')
                    if face3 == 'C':
                        cerebros = cerebros + 1
                    elif face3 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                elif dado3 == 'dVermelho':
                    face3 = random.choice(daVermelho)
                    print('O terceiro dado é Vermelho e você tirou um', face3, '\n')
                    if face3 == 'C':
                        cerebros = cerebros + 1
                    elif face3 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                else:
                    face3 = random.choice(daAmarelo)
                    print('O terceiro dado é Amarelo e você tirou um', face3, '\n')
                    if face3 == 'C':
                        cerebros = cerebros + 1
                    elif face3 == 'T':
                        tiros = tiros + 1
                    else:
                        passos = passos + 1

                # adiciona na lista de cada jogador as pontuações separadas
                cerebrojogador.append(cerebros)
                tirojogador.append(tiros)
                passojogador.append(passos)

                # soma a quantidade de cerebros, tiros e passos na lista e mostra somente o valor total
                somacerebros = sum(cerebrojogador)
                print('cerebros ->', somacerebros)

                somapassos = sum(passojogador)
                print('passos->', somapassos)

                somatiros = sum(tirojogador)
                print('tiros ->', somatiros, '\n')

                # se o jogador tomar mais de 3 tiros a rodada encerra e mostra a mensagem de que ele perdeu o jogo
                if somatiros > 2:
                    print(jogador, '**************** você tomou 3 tiros e PERDEU o jogo!********************* \n')
                    print('placar ->', placar, '\n')
                    jogadores.remove(jogador)
                    if len(jogadores) == 1:
                        print('************************ o outro jogador Venceu!***************************')
                        break

                sleep(1)

                # jogador escolhe depois de cada partida se quer continuar ou não
                escolha = input(f'{jogador} você quer continuar? sim/não \n')

                # se a escolha for sim o computador reinicia a rodada com o mesmo jogador
                if escolha == 'sim':
                    continue
                # se a resposta for não ele mostra o placar e finaliza a jogada passando para o próximo jogador
                else:
                    # armazena no dicionario a quantidade de cerebros de cada jogador
                    # dicionario para o placar de cada jogador mas somente dos cérebros
                    placar[jogador] = somacerebros + placar[jogador]
                    print('placar ->', placar, '\n')
                    if placar[jogador] >= 13:
                        print(jogador, '******************* VOCÊ VENCEU O JOGO *************************')
                        break

                    turno = True

            if jogadores == [jogador]:
                print(jogador, '******************* VOCÊ VENCEU O JOGO *************************')
                rodada = True
            else:
                continue
            if placar[jogador] >= 13:
                print(jogador, '******************* VOCÊ VENCEU O JOGO *************************')
                rodada = True
            else:
                continue
