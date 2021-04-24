'''
******************************************************************************************
Autor: Gabriel Cordeiro Moraes
Componente Curricular: EXA854 - MI - Algoritmos
Concluido em: 20/03/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
'''

from random import randint
from time import sleep
import keyboard
import os

#Gera a coluna em que o o meteoro aparece
def posicao_aleatoria_meteoro(colunas):
    posicao = randint(4, colunas-5) #Posição que o centro do meteoro aparece na tela
    return posicao


def objetos(numero_linhas, numero_colunas, centro_da_nave, posicao_aleatoria_meteoro, linha_referencia, linha_inicio_tiro, tiro_on, coluna_tiro):
    tela = [] #Matriz da tela
    vazio = str(' ')

    for i in range (numero_linhas):
        linha = [] #linha da matriz
        for j in range (numero_colunas):
            linha.append(vazio) #elementos que formam as colunas da matriz

        tela.append(linha)
    
    #Gera a nave na matriz
    for i in range(0, 3):
        if 3 <= centro_da_nave <= numero_colunas-3: # garante que a nave não saia do matriz
            tela[numero_linhas - 1][centro_da_nave + i] = 'x'
            tela[numero_linhas - 1][centro_da_nave - i] = 'x'
            
            if i < 2:
                tela[numero_linhas - 2][centro_da_nave + i] = 'x'
                tela[numero_linhas - 2][centro_da_nave - i] = 'x'
            
            if i < 1:
                tela[numero_linhas - 3][centro_da_nave] = 'x'
    
    #Gera o tiro na matriz
    if tiro_on == True:
        tela[linha_inicio_tiro][coluna_tiro] = 'o'
        
    coluna_referencia = posicao_aleatoria_meteoro-1 #coluna utilizada para gerar a hitbox do meteoro
    
    #Gera formato do meteoro
    for i in range(coluna_referencia,coluna_referencia + 3): #Laço que gera o retangulo do meteoro
        if linha_referencia <= numero_linhas:
            for j in range(0,5):
                tela[j+linha_referencia][i] = '*'
    
    for i in range(1,4):
        tela[i + linha_referencia][coluna_referencia-1] = '*'
        tela[i + linha_referencia][coluna_referencia+3] = '*'

    
    tela[2 + linha_referencia][coluna_referencia-2] = '*'
    tela[2 + linha_referencia][coluna_referencia+4] = '*'
    
    return tela


#printa a matriz que forma a tela
def atualiza_tela(matriz_da_tela, pontuacao, vidas):
    tela = matriz_da_tela
    os.system('cls')
    print('Pontos: %d' %pontuacao)
    print('Vidas: %d' %vidas)
    for linha in tela:
        print(''.join(linha))



def movimento_nave(centro_da_nave):

    while keyboard.is_pressed('left'):
        centro_da_nave -= 1
        return centro_da_nave
    
    while keyboard.is_pressed('right'):
        centro_da_nave += 1
        return centro_da_nave

    return centro_da_nave

def projetil(centro_da_nave, tiro_on, coluna_tiro):

    if keyboard.is_pressed('space'):
        
        coluna_tiro = centro_da_nave

        tiro_on = True
    
    return coluna_tiro, tiro_on

def colisao(tiro_on, linha_inicio_tiro, coluna_tiro, matriz_da_tela, contador_meteoro, linha_inicio_meteoro, numero_linhas, centro_da_nave, posicao_aleatoria_meteoro, vidas):
    
    colisao_tiro = False
    
    #Colisao do tiro
    if tiro_on == True and matriz_da_tela[linha_inicio_tiro][coluna_tiro] == '*':
        contador_meteoro = 0
        colisao_tiro = True
        return colisao_tiro, vidas
        
    
    if matriz_da_tela[numero_linhas-1][centro_da_nave-2] == '*':
        vidas = 0

    if matriz_da_tela[numero_linhas-1][centro_da_nave+2] == '*':
        vidas = 0

    if matriz_da_tela[numero_linhas-2][centro_da_nave-1] == '*':
        vidas = 0

    if matriz_da_tela[numero_linhas-2][centro_da_nave+1] == '*':
        vidas = 0
    
    if matriz_da_tela[numero_linhas-3][centro_da_nave] == '*':
        vidas = 0
    
    return colisao_tiro, vidas


    