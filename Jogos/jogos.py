import funcoes
from time import sleep
import forca
import adivinhacao

funcoes.titulo('BEM VINDO AO GAME LAB ')
print('(1) Forca \n(2) Advinhacao')
print()
jogo = int(input('ESCOLHA SEU JOGO: '))

if jogo == 1:
    print('Entrando no jogo da Forca ...')
    sleep(1)
    forca.jogar()
else:
    print('Entrando no jogo de Advinhação ....')
    sleep(1)
    adivinhacao.jogar()
