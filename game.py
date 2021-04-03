from meteoro import*
from time import sleep

numero_linhas = 20
numero_colunas = 20
game_on = True

while game_on:
    for i in range(2):
        movimento_meteoro(numero_linhas, numero_colunas, formato_meteoro())
        print("5 segundos")
        sleep(5)