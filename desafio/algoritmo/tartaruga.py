# importações
from turtle import *

# funções e classes
class tartaruga(Turtle):
    def __init__(self, cor, x, y):
        super().__init__()

        self.color(cor)
        self.penup()
        self.setposition(x, y)
        self.shape('turtle')

    def andar(self, x, y):
        self.goto(x, y)

# janela
janela = Screen()
janela.setup(900, 700)
janela.title("Desafio #turtle - Guilherme Monteiro")
janela.bgcolor('black')

# tartaruga
tartaruga = tartaruga('white', 0, 0)
# lendo o arquivo
arq = open('test.txt', 'r');
cont = 0

for linha in arq.readlines():
    separado = linha.split()
    # cima - posiciona (penup), baixo - desenha (pendown)
    if(cont == 1):
        tartaruga.andar(int(separado[0]), int(separado[1]))
    elif (separado[0] == 'CIMA'):
        tartaruga.penup()
    elif (separado[0] == 'BAIXO'):
        tartaruga.pendown()
    else:
        tartaruga.andar(int(separado[0]), int(separado[1]))
    cont += 1

janela.mainloop()