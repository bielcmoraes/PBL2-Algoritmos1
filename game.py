from tela import*
from random import randrange
import os        
from time import sleep
import keyboard

game_on = True
numero_linhas = 10
numero_colunas = 51
formato_meteoro = '0'
formato_nave = '+'
formato_tiro = 'o'


movimento(numero_linhas, numero_colunas, formato_meteoro, desenho_nave(), formato_tiro)
