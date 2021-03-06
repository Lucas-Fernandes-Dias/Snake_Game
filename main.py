import pygame
import random


class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)
    velocidade = 10
    posicao = (50, 10)
    ranking = []

    def __init__(self):

        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]
        self.direcao = 'direita'
        self.pontos = 0
        self.ranking = self.ranking

    def blit(self, screen):

        for posicao in self.corpo:
            screen.blit(self.textura, posicao)

    def andar(self):

        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        if self.direcao == 'direita':
            self.corpo.insert(0, (x + self.velocidade, y))

        elif self.direcao == 'esquerda':
            self.corpo.insert(0, (x - self.velocidade, y))
        elif self.direcao == 'cima':
            self.corpo.insert(0, (x, y - self.velocidade))
        elif self.direcao == 'baixo':
            self.corpo.insert(0, (x, y + self.velocidade))

        self.corpo.pop(-1)

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

    def colisao_frutinha(self, frutinha):
        if self.corpo[0] == frutinha.posicao:
            return True
        else:
            return False

    def colisao(self):
        cabeca = self.corpo[0]
        calda = self.corpo[1:]

        x = cabeca[0]
        y = cabeca[1]

        if x < 0 or y < 0 or x > 490 or y > 490 or cabeca in calda:
            self.ranking.append(self.pontos)
            pygame.display.set_caption('Snake / PONTOS: {}'.format(self.pontos))
            pygame.display.set_caption('Snake / MAIOR PONTUAÇÃO : {}'.format(max(self.ranking)))
            return True

    def comer(self):
        self.corpo.append((0, 0))
        self.pontos += 1
        pygame.display.set_caption('Snake / PONTOS: {}'.format(self.pontos))

    def game_over(self):
        screen.fill(vermelho)
        return True


class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self, cobrinha):

        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.posicao = Frutinha.criar_posicao(cobrinha)

    @staticmethod
    def criar_posicao(cobrinha):
        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10

        if (x, y) in cobrinha.corpo:
            Frutinha.criar_posicao(cobrinha)
        else:
            return x, y

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)



if __name__ == '__main__':
    pygame.init()
    resolucao = (500, 500)
    screen = pygame.display.set_mode(resolucao)
    clock = pygame.time.Clock()

    azul = (5, 50, 100)
    vermelho = (255, 0, 0)
    screen.fill(azul)

    cobrinha = Snake()

    frutinha = Frutinha(cobrinha)
    frutinha.blit(screen)

    while True:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cobrinha.cima()
                    break
                elif event.key == pygame.K_DOWN:
                    cobrinha.baixo()
                    break
                elif event.key == pygame.K_RIGHT:
                    cobrinha.direita()
                    break
                elif event.key == pygame.K_LEFT:
                    cobrinha.esquerda()

        if cobrinha.colisao_frutinha(frutinha):
            cobrinha.comer()
            frutinha = Frutinha(cobrinha)

        if cobrinha.colisao():
            cobrinha = Snake()

        cobrinha.andar()
        screen.fill(azul)
        cobrinha.blit(screen)
        frutinha.blit(screen)
        pygame.display.update()
