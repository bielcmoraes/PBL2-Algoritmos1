from random import randrange
import os
from time import sleep

def formato_meteoro():
    desenho = """
  *** 
 ***** 
******* 
 ***** 
  *** 
"""

    return desenho

def tela(numero_linhas, numero_colunas):
    
    tela = [] #Matriz da tela

    for i in range (numero_linhas):
        linha = [] #linha da matriz
        for j in range (numero_colunas):
            linha.append('') #elementos que formam as colunas da matriz

        tela.append(linha)

    return tela

def movimento_meteoro(numero_linhas, numero_colunas, objeto):
    meteoro = tela(numero_linhas, numero_colunas) #tela do game
    posicao = randrange(0,numero_colunas) #posicao aleatoria que o meteoro aparece na tela

    meteoro[0][posicao] = objeto #primeira linha da matriz com meteoro em posicao aleatoria
    
    for linha in meteoro:
        print(''.join(linha))
        sleep(0.006)

    for i in range(1,numero_linhas):
        meteoro[i-1][posicao] = ''
        meteoro[i][posicao] = objeto
        sleep(0.006)
        os.system('cls') #limpa o terminal para atualizar a tela
        os.system('cls')
    
        for linha in meteoro:
            print(''.join(linha))
            sleep(0.012)
            
   
        os.system("cls")
        os.system("cls")