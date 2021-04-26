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
import keyboard
import os
from time import sleep
from game import *

os.system("mode con: cols=45 lines=37")
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

    print('''
    _       _               _    _    
   /_\   __| |_ ___ _ _ ___(_)__| |___
  / _ \ (_-<  _/ -_) '_/ _ \ / _` (_-<
 /_/ \_\/__/\__\___|_| \___/_\__,_/__/
                                      
''')
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

record = []
while True:
    contador = controles(contador)
    menu(contador)

    if keyboard.is_pressed('enter') and menu(contador) == 0:
        sleep(0.1)
        (nome, pontuacao) = game()
        dados = (nome, pontuacao)
        record.append(dados)
    
    elif keyboard.is_pressed('enter') and menu(contador) == 1:
        while not keyboard.is_pressed('Esc'):
            try:
                os.system('cls')
                recordes_ordenados = recorde(nome, pontuacao,record)
                print('''
  ___                   _        
 | _ \___ __ ___ _ _ __| |___ ___
 |   / -_) _/ _ \ '_/ _` / -_|_-<
 |_|_\___\__\___/_| \__,_\___/__/
                                 
''')
                for i in range(len(recordes_ordenados)):
                    if i <= 5:
                        print(recordes_ordenados[i])
                
                print('Pressione "Esc" para continuar')
                sleep(1)
            
            except NameError:
                os.system('cls')
                print('''
  ___                   _        
 | _ \___ __ ___ _ _ __| |___ ___
 |   / -_) _/ _ \ '_/ _` / -_|_-<
 |_|_\___\__\___/_| \__,_\___/__/
                                 
''')
                print('Não existe puntuação ainda.')
                sleep(1)
                
        
        if keyboard.is_pressed('esc'):
            keyboard.press('esc')
            
    elif keyboard.is_pressed('enter') and menu(contador) == 2:
        sleep(0.1)
        while not keyboard.is_pressed('esc'):
            os.system('cls')
            print('''
 __ _     _     _  _  __
/  / \|V||_||\|| \/ \(_ 
\__\_/| || || ||_/\_/__)
''')
            
            print('Left: Move a nave para esquerda\n')
            print('Right: Move a nave para a direita\n')
            print('Space: Dispara um projétil\n')
            print('Esc: Finaliza a partida\n')
            print('''                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       ''')
            print('By: Gabriel Moraes')
            sleep(1)
    
    elif keyboard.is_pressed('enter') and menu(contador) == 3:
        sleep(0.1)
        exit()