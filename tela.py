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

from random import randint
import keyboard
import os

#Gera uma coluna aleatória como referencia para o surgimento do meteoro
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
            
            #Gera a primeira linha de caracteres da nave
            tela[numero_linhas - 1][centro_da_nave + i] = 'x'
            tela[numero_linhas - 1][centro_da_nave - i] = 'x'
            
            #Gera a segunda linha de caracteres da nave
            if i < 2:
                tela[numero_linhas - 2][centro_da_nave + i] = 'x'
                tela[numero_linhas - 2][centro_da_nave - i] = 'x'
            
            #Gera o "topo" da nave
            if i < 1:
                tela[numero_linhas - 3][centro_da_nave] = 'x'
    
    #Gera o tiro na matriz
    if tiro_on == True:
        tela[linha_inicio_tiro][coluna_tiro] = 'o' #Gera o caractere do projetil na matriz
        
    coluna_referencia = posicao_aleatoria_meteoro-1 #coluna utilizada para gerar a hitbox do meteoro
    
    #Gera formato do meteoro
    for i in range(coluna_referencia,coluna_referencia + 3): #Laço que gera o retangulo do meteoro
        if linha_referencia <= numero_linhas:
            for j in range(0,5):
                tela[j+linha_referencia][i] = '*'
    
    for i in range(1,4): #Laço que gera duas colunas de caracteres do meteoro
        tela[i + linha_referencia][coluna_referencia-1] = '*'
        tela[i + linha_referencia][coluna_referencia+3] = '*'

    # Caracteres "individuais" do meteoro
    tela[2 + linha_referencia][coluna_referencia-2] = '*'
    tela[2 + linha_referencia][coluna_referencia+4] = '*'
    
    return tela


#printa a matriz que forma a tela
def atualiza_tela(matriz_da_tela, pontuacao, vidas):
    tela = matriz_da_tela
    os.system('cls') #limpa a tela
    print('Pontos: %d' %pontuacao) #Mostra a pontuação
    print('Vidas: %d' %vidas) #Mostra a vida do jogador na tela
    for linha in tela:
        print(''.join(linha)) #Mostra a linha da matriz



def movimento_nave(centro_da_nave):
    # Movimenta a nave caso as teclas "left" e "right" sejam pressionadas
    while keyboard.is_pressed('left'): 
        centro_da_nave -= 2
        return centro_da_nave
    
    while keyboard.is_pressed('right'):
        centro_da_nave += 2
        return centro_da_nave

    return centro_da_nave

def projetil(centro_da_nave, tiro_on, coluna_tiro):
    # Gera um projétil na tela caso a tecla "space" seja pressionada
    if keyboard.is_pressed('space'):
        
        coluna_tiro = centro_da_nave

        tiro_on = True
    
    return coluna_tiro, tiro_on

def colisao(tiro_on, linha_inicio_tiro, coluna_tiro, matriz_da_tela, contador_meteoro, linha_inicio_meteoro, numero_linhas, numero_colunas, centro_da_nave, posicao_aleatoria_meteoro, vidas):
    
    colisao_tiro = False
    
    #Colisao do tiro com o meteoro
    if tiro_on == True and matriz_da_tela[linha_inicio_tiro][coluna_tiro] == '*':
        contador_meteoro = 0
        colisao_tiro = True
        return colisao_tiro, vidas
        
    # Colisão da nave com o meteoro
    if 3 <= centro_da_nave <= numero_colunas-3: #Garente que a verificação será feita com a nave dentro da matriz
        if matriz_da_tela[numero_linhas-1][centro_da_nave-2] == '*':
            vidas = 10

        if matriz_da_tela[numero_linhas-1][centro_da_nave+2] == '*':
            vidas = 10

        if matriz_da_tela[numero_linhas-2][centro_da_nave-1] == '*':
            vidas = 10

        if matriz_da_tela[numero_linhas-2][centro_da_nave+1] == '*':
            vidas = 10
        
        if matriz_da_tela[numero_linhas-3][centro_da_nave] == '*':
            vidas = 10
    
    return colisao_tiro, vidas


    