
import pygame

class Labirinto:
    def __init__(self, imagem_path):
        self.imagem = pygame.image.load(imagem_path)
        self.largura, self.altura = self.imagem.get_size()
        self.posicaoSaida = (self.largura - 50, self.altura - 50)

    def carregar(self, screen):
        screen.blit(self.imagem, (0, 0))

    def verificarColisao(self, personagem_rect):
        # Aqui você pode implementar colisão com paredes se quiser
        return False
