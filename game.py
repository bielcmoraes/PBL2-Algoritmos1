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
    # linha_referencia_meteoro = 0 #Gera o primeiro meteoro da partida na primeira linha
    tiro_on = False
    coluna_tiro = 0
    pontuacao = 0
    vidas = 0

    while True:
        linha_referencia_meteoro = 0
        linha_inico_tiro = linhas - 3
        contador_geral = 0
        contador_meteoro = 0
        contador_tiro = 0
        posicao = posicao_aleatoria_meteoro(colunas)

        while contador_geral >= 0:
            
            matriz_tela = objetos(linhas, colunas, centro_nave, posicao, linha_referencia_meteoro, linha_inico_tiro, tiro_on, coluna_tiro)
            
            atualiza_tela(matriz_tela, pontuacao, vidas)

            centro_nave = movimento_nave(centro_nave)

            (coluna_tiro,tiro_on) = projetil(centro_nave, tiro_on, coluna_tiro)

            if tiro_on:
                if linha_inico_tiro > 1:
                    linha_inico_tiro -= contador_tiro
                    
                    
                else:
                    tiro_on = False
                    linha_inico_tiro = linhas - 3
                    contador_tiro = 0
                
            sleep(0.2)
            linha_referencia_meteoro = contador_meteoro

            (colisao_tiro, vidas)= colisao(tiro_on, linha_inico_tiro, coluna_tiro, matriz_tela,contador_meteoro, linha_referencia_meteoro, linhas, colunas, centro_nave, posicao,vidas)
            if colisao_tiro:
                tiro_on = False
                contador_meteoro = 0
                contador_tiro = 0
                pontuacao +=10
                break

            clock_meteoro = contador_geral //2
            
            if clock_meteoro == 0:
                contador_meteoro +=1
            
            contador_tiro +=1

            if contador_meteoro > linhas-5: # Evita que meteoro saia do range
                contador_meteoro = 0
                vidas += 1
                break
            
            if vidas >= 10 or keyboard.is_pressed('esc'):
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
                while desbugar != '321':
                    input('')
                    if keyboard.is_pressed('enter'):
                        desbugar = '321'
                nome = input('Digite seu nome: ')
                return nome , pontuacao

            if contador_geral > 40: # Reseta o contador para evitar aumento infinito
                contador_geral = 0


def recorde(nome, pontuacao, record):
    valores_ordenados = sorted(record, key = lambda item:item[1], reverse = True)
    return valores_ordenados