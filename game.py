'''
******************************************************************************************
Autor: Gabriel Cordeiro Moraes
Componente Curricular: EXA854 - MI - Algoritmos
Concluido em: 26/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
'''
from time import sleep
from tela import *
import os
import keyboard

def game():

    linhas = 34 #Número de linhas da matriz da tela
    colunas = 35 #Número de colunas da matriz
    centro_nave = colunas // 2 +1 #Gera a nave no centro da tela no inicio da partida
    tiro_on = False
    coluna_tiro = 0 #Inicialização de variavél 
    pontuacao = 0
    vidas = 0 #Numero de meteoros que chegaram ao final da tela

    while True:

        linha_referencia_meteoro = 0 #Linha em que o meteoro é gerado
        linha_inico_tiro = linhas - 3 #Linha inicial do tiro
        
        #Inicialização de variaveis
        contador_geral = 0
        contador_meteoro = 0
        contador_tiro = 0
        posicao = posicao_aleatoria_meteoro(colunas) #Posição aleatória do meteoro

        while contador_geral >= 0:
            
            matriz_tela = objetos(linhas, colunas, centro_nave, posicao, linha_referencia_meteoro, linha_inico_tiro, tiro_on, coluna_tiro) #Controi todos os objetos na tela
            
            atualiza_tela(matriz_tela, pontuacao, vidas) #Printa todos os objetos na tela

            centro_nave = movimento_nave(centro_nave) #Movimento da nave

            (coluna_tiro,tiro_on) = projetil(centro_nave, tiro_on, coluna_tiro) #Tiro da nave

            if tiro_on:

                if linha_inico_tiro > 1: #Garante que o tiro não saia do range
                    linha_inico_tiro -= contador_tiro #Movimenta o tiro na tela 
                    
                    
                else:
                    #reinicia as variaveis
                    tiro_on = False

                    linha_inico_tiro = linhas - 3 

                    contador_tiro = 0
                
            sleep(0.2)

            linha_referencia_meteoro = contador_meteoro # Movimenta o meteoro na tela 

            (colisao_tiro, vidas)= colisao(tiro_on, linha_inico_tiro, coluna_tiro, matriz_tela,contador_meteoro, linha_referencia_meteoro, linhas, colunas, centro_nave, posicao,vidas) #verifica se houve colisão

            if colisao_tiro: #Reinicia as variavéis 

                tiro_on = False

                contador_meteoro = 0

                contador_tiro = 0

                pontuacao +=10 #Incrementa a pontuação

                break

            clock_meteoro = contador_geral //2 #Velocidade do meteoro
            
            if clock_meteoro == 0: #Garante que velocidade do meteoro seja metade da velocidade do resto das funções
                contador_meteoro +=1
            
            contador_tiro +=1

            if contador_meteoro > linhas-5: # Evita que meteoro saia do range

                contador_meteoro = 0

                vidas += 1
                break
            
            if vidas >= 10 or keyboard.is_pressed('esc'): #Finaliza a partida caso pressione "Esc" ou 10 meteoros cheguem ao solo

                keyboard.press('esc')

                os.system('cls')

                print('''
    ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██║  ███╗███████║██╔████╔██║█████╗  
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                        
    ''')
                print('''
    ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                    
    ''')  
                desbugar = 'abacaxi'
                print('Pressione "Enter" para continuar')
                while desbugar != '321': #"Limpa" as teclas pressionadas durante a partida 
                    input('')

                    if keyboard.is_pressed('enter'):
                        desbugar = '321'

                nome = input('Digite seu nome: ')

                return nome , pontuacao #Retorna o nome e a pontuação do jogador em caso de "Game Over"

            if contador_geral > 40: # Reseta o contador para evitar aumento infinito
                contador_geral = 0


def recorde(nome, pontuacao, record):

    #Ordena os recordes do maior para o menor de acordo com o segundo elemento da tupla
    valores_ordenados = sorted(record, key = lambda item:item[1], reverse = True)

    return valores_ordenados