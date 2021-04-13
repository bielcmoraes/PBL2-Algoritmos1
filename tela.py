from random import randint
import os
from time import sleep
import keyboard

def meteoros(numero_linhas, numero_colunas, posicao, linha_referencia, centro_da_nave, referencia_tiro, projetil):
    tela = [] #Matriz da tela
    vazio = str(' ')

    for i in range (numero_linhas):
        linha = [] #linha da matriz
        for j in range (numero_colunas):
            linha.append(vazio) #elementos que formam as colunas da matriz

        tela.append(linha)

    coluna_referencia = posicao-1 #coluna utilizada para gerar a hitbox do meteoro
    
    #Gera formato do meteoro
    for i in range(coluna_referencia,coluna_referencia + 3): #Laço que gera o retangulo do meteoro
        if linha_referencia <= numero_linhas:
            for j in range(0,5):
                tela[j+linha_referencia][i] = '▪'
    
    for i in range(1,4):
        tela[i + linha_referencia][coluna_referencia-1] = '▪'
        tela[i + linha_referencia][coluna_referencia+3] = '▪'

    tela[2 + linha_referencia][coluna_referencia-2] = '▪'
    tela[2 + linha_referencia][coluna_referencia+4] = '▪'
    
  
    #Gera a nave na matriz
    
    for i in range(0, 3):
        if 3 <= centro_da_nave <= numero_colunas-3: # garante que a nave não saia do matriz
            tela[numero_linhas - 1][centro_da_nave + i] = '█'
            tela[numero_linhas - 1][centro_da_nave - i] = '█'
            
            if i < 2:
                tela[numero_linhas - 2][centro_da_nave + i] = '█'
                tela[numero_linhas - 2][centro_da_nave - i] = '█'
            
            if i < 1:
                tela[numero_linhas - 3][centro_da_nave] = '█'
            
    #Gera o tiro na matriz
    for i in range(4, numero_linhas):
        if 3 <= centro_da_nave <= numero_colunas-3:
            if keyboard.is_pressed('space'):
                tela[numero_linhas- i][centro_da_nave] = '|'
    
            
    return tela


def posicao_aleatoria_meteoro(colunas):
    posicao = randint(3, colunas-3) #Posição que o centro do meteoro aparece na tela
    return posicao

#printa a matriz que forma a tela
def atualiza_tela(matriz_da_tela):
    tela = matriz_da_tela
    for linha in tela:
        print(''.join(linha))


def movimento_nave(centro_da_nave):

    while keyboard.is_pressed('left'):
        centro_da_nave -= 3
        return centro_da_nave
    
    while keyboard.is_pressed('right'):
        centro_da_nave += 3
        return centro_da_nave
    
    return centro_da_nave

def projetil():
    if keyboard.is_pressed('space'):
        return True