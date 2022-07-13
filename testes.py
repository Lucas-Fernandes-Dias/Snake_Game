import pygame
import random
import time


pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
azul = (5, 50, 100)


class Snake:

    cor = (255, 255, 255)
    tamanho = (10, 10)
    velocidade = 10

    def __init__(self):

        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]
        self.direcao = 'direita'

    def blit(self, screen):

        for posicao in self.corpo:
            screen.blit(self.textura, posicao)

    def andar(self):

        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]
        time.sleep(0.03)

        if self.direcao == 'direita':
            self.corpo[0] = (x + self.velocidade, y)
        elif self.direcao == 'esquerda':
            self.corpo[0] = (x - self.velocidade, y)
        elif self.direcao == 'cima':
            self.corpo[0] = (x, y - self.velocidade)
        elif self.direcao == 'baixo':
            self.corpo[0] = (x, y + self.velocidade)

    def cima(self):
        if self.direcao != 'baixo':
            self.direcao = 'cima'

    def baixo(self):
        if self.direcao != 'cima':
            self.direcao = 'baixo'

    def esquerda(self):
        if self.direcao != 'direita':
            self.direcao = 'esquerda'

    def direita(self):
        if self.direcao != 'esquerda':
            self.direcao = 'direita'



class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)


frutinha = Frutinha()
snaker = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if pygame.key.get_pressed():
            if event.type == pygame.K_UP:
                snaker.cima()
            if event.type == pygame.K_DOWN:
                snaker.baixo()
            if event.type == pygame.K_RIGHT:
                snaker.direita()
            if event.type == pygame.K_LEFT:
                snaker.esquerda()


    snaker.andar()
    screen.fill(azul)
    snaker.blit(screen)

    frutinha.blit(screen)



    pygame.display.update()
