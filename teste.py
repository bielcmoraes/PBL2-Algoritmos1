from pynput.keyboard import Listener


def Capturar(tecla):
    tecla = str(tecla)
    if tecla == 'Key.up':
        print(tecla)

with Listener(on_press = Capturar) as evento:
    evento.join()