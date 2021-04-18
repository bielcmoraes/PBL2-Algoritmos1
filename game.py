from time import sleep
from tela import *
import os
import keyboard

linhas = 34
colunas = 35
centro_nave = colunas // 2 +1
linha_referencia_meteoro = 0
tiro_on = False
coluna_tiro = 0
pontuacao = 0
vidas = 10

while True:
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
            
        
        linha_referencia_meteoro = contador_meteoro

        if colisao(tiro_on, linha_inico_tiro, coluna_tiro, matriz_tela,contador_meteoro, linha_referencia_meteoro, linhas, centro_nave, posicao):
            tiro_on = False
            contador_geral = 0
            contador_meteoro = 0
            contador_tiro = 0
            sleep(0.1)
            pontuacao +=10
            break

        clock_meteoro = contador_geral //2
        
        if clock_meteoro == 0:
            contador_meteoro +=1
        
        contador_tiro +=1

        if contador_meteoro > linhas-5: # Evita que meteoro saia do range
            contador_meteoro = 0
            vidas -= 1
        
        if vidas == 0 or keyboard.is_pressed('esc'):
            print('Game Over')
            exit()
        

        if contador_geral > 40: # Reseta o contador para evitar aumento infinito
            contador_geral = 0