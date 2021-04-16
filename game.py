from tela import*
import os        
from time import sleep
import keyboard

centro_da_nave = (63 // 2) + 1

def principal(centro_da_nave):
    game_on = True
    linhas = 25
    colunas = 63
    linha_inicio_tiro = linhas - 4
    
    linha_final_meteoro = linhas - 4
   
    posicao_inicial_meteoro = posicao_aleatoria_meteoro(colunas)

    movimento = 0
    inicio_meteoro = 0

    for movimento in range(0, linhas):

        clock = movimento % 5

        matriz_vazia = gera_matriz(linhas, colunas) #Gera matriz mazia
        centro_da_nave = movimento_nave(centro_da_nave) #retorna a posicao da nave a cada mudança
        posicao_tiro = centro_da_nave
        tela_nave = nave(linhas, colunas, matriz_vazia, centro_da_nave) # Gera a nave na tela
        # controle_tiro = projetil() #Controla o tiro

        if clock == 0:

            inicio_meteoro = movimento
            tela_final = meteoros(linhas, colunas, tela_nave, posicao_inicial_meteoro, inicio_meteoro) #Gera o meteoro na tela

            atualiza_tela(tela_final) #Imprime a ultima tela
            sleep(0.9)
            
        
        if 0 <= clock:
            if linha_inicio_tiro > 1:

                tela_tiro = tiro(linha_inicio_tiro, colunas, tela_final, projetil(),posicao_tiro) #Gera o tiro na tela

                linha_inicio_tiro -= movimento

                atualiza_tela(tela_final) #Imprime a ultima tela
    
    return centro_da_nave
            

while True:
    centro_da_nave = principal(centro_da_nave)