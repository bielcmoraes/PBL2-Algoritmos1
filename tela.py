from random import randrange
import os
from time import sleep
import keyboard

def desenho_meteoro():
    desenho = """
  *** 
 ***** 
******* 
 ***** 
  *** 
"""

    return desenho

def desenho_nave():
    desenho = '∆'
    return desenho


def tela(numero_linhas, numero_colunas):
    
    tela = [] #Matriz da tela
    centro_da_tela = (numero_colunas//2) + 1
    vazio = str(' ')

    for i in range (numero_linhas):
        linha = [] #linha da matriz
        for j in range (numero_colunas):
            linha.append(vazio) #elementos que formam as colunas da matriz

        tela.append(linha)

    return tela

def movimento(numero_linhas, numero_colunas, formato_meteoro, formato_nave,formato_tiro):
    centro_da_tela = (numero_colunas//2) + 1

    matriz_tela = tela(numero_linhas, numero_colunas) #tela do game
    posicao = randrange(0,numero_colunas) #posicao aleatoria que o meteoro aparece na tela
    matriz_tela[0][posicao] = formato_meteoro #primeira linha da matriz com meteoro em posicao aleatoria
    matriz_tela [numero_linhas-1][centro_da_tela] = formato_nave #gera a nave na matriz
    vazio = str('')

    while True:

        for linha in matriz_tela:
                teste = ''.join(linha)
                teste.replace('\n','')
                print(teste)

        for i in range(1,numero_linhas):
            matriz_tela[i-1][posicao] = vazio
            matriz_tela[i][posicao] = formato_meteoro
            matriz_tela [numero_linhas-1][centro_da_tela] = formato_nave
        
            if keyboard.is_pressed('space'): #atira se apertar espaco
                matriz_tela[numero_linhas-i][centro_da_tela] = formato_tiro
                os.system('cls') #limpa o terminal para atualizar a tela
            os.system('cls')

            if keyboard.is_pressed('left'): #move a nave para esquerda
                
                matriz_tela[numero_linhas-1][centro_da_tela] = ''
                centro_da_tela -= 10
                matriz_tela[numero_linhas-1][centro_da_tela] = formato_nave
                os.system("cls")
            
            if keyboard.is_pressed('right'): #move a nave para a direita

                matriz_tela[numero_linhas-1][centro_da_tela] = ''
                centro_da_tela += 10
                matriz_tela[numero_linhas-1][centro_da_tela] = formato_nave
                os.system("cls")
            
            print('_'*numero_colunas)
            for linha in matriz_tela:
                teste = ''.join(linha)
                teste.replace('\n','')
                print(teste)
                sleep(0.016)
                
            os.system("cls")