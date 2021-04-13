from tela import*
import os        
from time import sleep
import keyboard

game_on = True
linhas = 40
colunas = 65
linha_inicio_meteoro = 0
posicao_inicial_meteoro = posicao_aleatoria_meteoro(colunas)
centro_da_nave = (colunas // 2) + 1
linha_inicio_tiro = linhas - 1

while game_on:
    if not keyboard.is_pressed('esc'):
        
        for movimento in range(0, linhas-4):
            clock = movimento % 5 #Clock em 5 que garante que o laço só seja executado nos ranges multipos de 5
    
            centro_da_nave = movimento_nave(centro_da_nave)

            linha_inicio_tiro = movimento_nave(centro_da_nave)

            tiro = projetil()

            tela_atual = meteoros(linhas, colunas, posicao_inicial_meteoro, linha_inicio_meteoro,centro_da_nave,linha_inicio_tiro, tiro)

            linha_inicio_meteoro = movimento
        
            linha_inicio_tiro += movimento
            if clock != 0:
                os.system('cls')
                atualiza_tela(tela_atual)
                sleep(0.3)
    else:
        game_on = False 