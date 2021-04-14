from tela import*
import os        
from time import sleep
import keyboard

game_on = True
linhas = 40
colunas = 65
linha_inicio_meteoro = 0
centro_da_nave = (colunas // 2) + 1
linha_inicio_tiro = linhas - 1

while game_on:
    if not keyboard.is_pressed('esc'):
        posicao_inicial_meteoro = posicao_aleatoria_meteoro(colunas)
        
        for movimento in range(0, linhas-4):
            clock = movimento % 5 #Clock em 5 que garante que o laço só seja executado nos ranges multipos de 5

            matriz_vazia = gera_matriz(linhas, colunas) #Gera matriz mazia
    
            centro_da_nave = movimento_nave(centro_da_nave) #retorna a posicao da nave a cada mudança

            linha_inicio_tiro = movimento_nave(centro_da_nave)

            controle_nave = movimento_nave(centro_da_nave) #Controla a posição da nave

            tela_nave = nave(linhas, colunas, matriz_vazia, centro_da_nave) # Gera a nave na tela

            controle_tiro = projetil() #Controla o tiro

            controle_colisao = colisao(controle_tiro, posicao_inicial_meteoro, centro_da_nave)

            ultima_tela = tiro(linhas, colunas, tela_nave, controle_tiro, centro_da_nave) #Gera o tiro na tela

            tela_meteoro = meteoros(linhas, colunas, tela_nave, posicao_inicial_meteoro, linha_inicio_meteoro, controle_colisao) #Gera o meteoro na tela
            
            controle_colisao = colisao(controle_tiro, posicao_inicial_meteoro, centro_da_nave)

            if controle_colisao == True:
                if clock != 0:
                    os.system('cls')
                atualiza_tela(tela_nave) #Imprime a ultima tela
                sleep(0.3)
                break
            
            else:

                linha_inicio_meteoro = movimento
            
                linha_inicio_tiro += movimento
                
                if clock != 0:
                    os.system('cls')
                    atualiza_tela(ultima_tela) #Imprime a ultima tela
                    sleep(0.3)
    else:
        game_on = False 