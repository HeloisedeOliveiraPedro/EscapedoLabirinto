import pygame

class Tela:
    def __init__(self, tipo, fundo):
        self.tipo = tipo
        self.fundo = pygame.image.load(fundo)

    def exibir(self, screen):
        screen.blit(self.fundo, (0, 0))

    def desenharTexto(self, texto, fonte, cor, x, y, screen):
        texto_render = fonte.render(texto, True, cor)
        texto_rect = texto_render.get_rect(center=(x, y))
        screen.blit(texto_render, texto_rect)

    def desenharBotao(self, rect, cor, texto, fonte, texto_cor, screen):
        pygame.draw.rect(screen, cor, rect)
        self.desenharTexto(texto, fonte, texto_cor, rect.centerx, rect.centery, screen)