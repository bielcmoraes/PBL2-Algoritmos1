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
import keyboard
import os
from time import sleep
from game import *

os.system("mode con: cols=45 lines=37") #Limita o tamanho da janela do terminal

#Cria a matriz do menu
def menu(contador_selecionar):
    tela_menu = []
    vazio = str(' ')
    for i in range(0,4):
        linha = []
        for j in range(3):
            linha.append(vazio)
        
        tela_menu.append(linha)


    tela_menu[0][1] = 'JOGAR'
    tela_menu[1][1] = 'RECORDES'
    tela_menu[2][1] = 'SOBRE'
    tela_menu[3][1] = 'SAIR'

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
    
    print('''
        _..._
      .'     '.      _
     /    .-""-\   _/ \\
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|ECOMP_.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\\
\__/'._;.  ==' ==\\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \\
          `-._/._/''')
    
    print('Art by: jgs')
    
    sleep(0.1)
    os.system('cls')
    return contador_selecionar


def controles(contador_selecionar):

    #Controla e movimenta a seleção do menu
    if keyboard.is_pressed('down'):
        contador_selecionar+=1
        if contador_selecionar > 3:
            contador_selecionar = 0
    
    if keyboard.is_pressed('Up'):
        contador_selecionar -=1
        if contador_selecionar < 0:
            contador_selecionar = 3
        
    
    return contador_selecionar


contador = 0 #Contador do menu

record = [] #Guarda o nome e a pontuação dos jogadores
while True:
    contador = controles(contador)
    menu(contador)

    #Inicia partida caso o usuario selecione "Jogar"
    if keyboard.is_pressed('enter') and menu(contador) == 0:
        (nome, pontuacao) = game()
        dados = (nome, pontuacao)
        record.append(dados)
    
    #Mostra os recordes caso o usuario selecione "Recordes"
    elif keyboard.is_pressed('enter') and menu(contador) == 1:
        while not keyboard.is_pressed('Esc'): #Caso o usuario aperte "Esc" retorna ao menu
            try:
                os.system('cls')
                recordes_ordenados = recorde(nome, pontuacao,record) #Ordena os recordes do maior para o menor
                print('''
  ___                   _        
 | _ \___ __ ___ _ _ __| |___ ___
 |   / -_) _/ _ \ '_/ _` / -_|_-<
 |_|_\___\__\___/_| \__,_\___/__/
                                 
''')
                for i in range(len(recordes_ordenados)):
                    if i < 5: #Garante que o print seja dos 5 primeiros colocados
                        print(recordes_ordenados[i][0],'-----',recordes_ordenados[i][1])
                
                print('\nPressione "Esc" para retornar ao Menu')
                sleep(1)
            
            #Caso a lista esteja vazia e a função de ordenar retorne um NameError indica que não há recods cadastrados
            except NameError: 
                os.system('cls')
                print('''
  ___                   _        
 | _ \___ __ ___ _ _ __| |___ ___
 |   / -_) _/ _ \ '_/ _` / -_|_-<
 |_|_\___\__\___/_| \__,_\___/__/
                                 
''')
                print('Não existe puntuação ainda.')
                print('\nPressione "Esc" para retornar ao Menu')
                sleep(1)
                
        
        if keyboard.is_pressed('esc'):
            keyboard.press('esc')

    #Mostra o sobre caso o usuario selecione "Sobre"        
    elif keyboard.is_pressed('enter') and menu(contador) == 2:
        while not keyboard.is_pressed('esc'): #Caso o usuario aperte "Esc" retorna ao menu
            os.system('cls')
            print('''
 __ _     _     _  _  __
/  / \|V||_||\|| \/ \(_ 
\__\_/| || || ||_/\_/__)
''')
            
            print('Left: Move a nave para esquerda\n')
            print('Right: Move a nave para a direita\n')
            print('Space: Dispara um projétil\n')
            print('Esc: Voltar/finalizar a partida\n')
            print('''                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       ''')
            print('Art by: jgs')
            print('\nGame By: Gabriel Moraes')
            sleep(1)
    
    #Sai do programa cso o usuario selecione sair
    elif keyboard.is_pressed('enter') and menu(contador) == 3:
        print('\n Até a próxima\n')
        sleep(5)
        exit()