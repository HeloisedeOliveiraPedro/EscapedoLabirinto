import pygame
import random

class Personagem:
    def __init__(self, nome, imagem_path):
        self.nome = nome
        self.imagem = pygame.image.load(imagem_path)
        self.imagem = pygame.transform.scale(self.imagem, (32, 32))
        self.posicaoX = random.randint(0, 600 - 32)
        self.posicaoY = random.randint(0, 480 - 32)

    def mover(self, direcao):
        if direcao == "cima":
            self.posicaoY -= 5
        elif direcao == "baixo":
            self.posicaoY += 5
        elif direcao == "esquerda":
            self.posicaoX -= 5
        elif direcao == "direita":
            self.posicaoX += 5

    def definirPosicaoAleatoria(self):
        self.posicaoX = random.randint(0, 600 - 32)
        self.posicaoY = random.randint(0, 480 - 32)
