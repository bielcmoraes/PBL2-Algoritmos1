import keyboard
import os
from time import sleep

def menu(contador_selecionar):
    tela_menu = []
    vazio = str(' ')
    for i in range(0,4):
        linha = []
        for j in range(3):
            linha.append(vazio)
        
        tela_menu.append(linha)


    tela_menu[0][1] = 'Jogar'
    tela_menu[1][1] = 'Recordes'
    tela_menu[2][1] = 'Sobre'
    tela_menu[3][1] = 'Sair'

    tela_menu[contador_selecionar][0] = '>'
    tela_menu[contador_selecionar][2] = '<'

    for linha in tela_menu:
        print(''.join(linha))
    
    sleep(0.1)
    os.system('cls')
    return contador_selecionar

def controles(contador_selecionar):

    if keyboard.is_pressed('down'):
        contador_selecionar+=1
        if contador_selecionar > 3:
            contador_selecionar = 0
    
    if keyboard.is_pressed('Up'):
        contador_selecionar -=1
        if contador_selecionar < 0:
            contador_selecionar = 3
        
    
    return contador_selecionar


contador = 0
while True:
    contador = controles(contador)
    menu(contador)

    if keyboard.is_pressed('enter') and menu(contador) == 0:
        print('Bora jogar')
        break
    
    elif keyboard.is_pressed('enter') and menu(contador) == 1:
        print('recordes aqui')
        break
    
    elif keyboard.is_pressed('enter') and menu(contador) == 2:
        print('Sobre aqui')
        break
    
    elif keyboard.is_pressed('enter') and menu(contador) == 3:
        sleep(0.1)
        exit()