import pygame
import time
from personagem import Personagem
from labirinto import Labirinto
from tela import Tela
import sys
import os


class Jogo:
    def __init__(self):
        pygame.init()  # Inicializa pygame
        self.nome = "Escape do Labirinto"
        self.tempo = 0
        self.estado = "inicio"
        self.screen = pygame.display.set_mode((1024, 780))
        pygame.display.set_caption(self.nome)
        self.fonte = pygame.font.SysFont(None, 48)
        self.fonte_pequena = pygame.font.SysFont(None, 36)

        # Carregar personagem com fallback
        try:
            self.personagem = Personagem("Jogador", "assets/personagem.png")
        except pygame.error:
            print("⚠️ Erro: Não encontrei 'assets/personagem.png'. Usando quadrado vermelho como personagem.")
            surf = pygame.Surface((32, 32))
            surf.fill((255, 0, 0))
            self.personagem = type("TempPersonagem", (), {})()  # cria objeto simples
            self.personagem.imagem = surf
            self.personagem.posicaoX = 50
            self.personagem.posicaoY = 50
            self.personagem.mover = lambda d: None  # não se move

        # Carregar labirinto com fallback
        try:
            self.labirinto = Labirinto("assets/labirinto.jpg")
        except pygame.error:
            print('⚠️ Erro: Não encontrei \'assets/labirinto.jpg\'. Usando fundo cinza.')
            surf = pygame.Surface((1024, 780))
            surf.fill((100, 100, 100))
            self.labirinto = type("TempLabirinto", (), {})()
            self.labirinto.imagem = surf
            self.labirinto.posicaoSaida = (550, 430)
            self.labirinto.carregar = lambda screen: screen.blit(surf, (0, 0))

        # Carregar tela com fallback
        try:
            self.tela = Tela("inicio", "assets/fundo.jpg")
        except pygame.error:
            print('⚠️ Erro: Não encontrei \'assets/fundo.jpg\'. Usando fundo preto.')
            surf = pygame.Surface((1024, 780))
            surf.fill((0, 0, 0))
            self.tela = type("TempTela", (), {})()
            self.tela.exibir = lambda screen: screen.blit(surf, (0, 0))
            self.tela.desenharTexto = Tela.desenharTexto
            self.tela.desenharBotao = Tela.desenharBotao

        self.clock = pygame.time.Clock()
        self.start_button = pygame.Rect(225, 300, 150, 50)

    def iniciar(self):
        self.tela.exibir(self.screen)
        self.tela.desenharTexto(self.nome, self.fonte, (255, 255, 255), 300, 200, self.screen)
        self.tela.desenharBotao(self.start_button, (255, 255, 255), "START", self.fonte_pequena, (0, 0, 0), self.screen)
        pygame.display.flip()

        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        esperando = False
                        self.estado = "jogando"
                        self.atualizar()

    def atualizar(self):
        inicio = time.time()
        while self.estado == "jogando":
            self.labirinto.carregar(self.screen)
            self.screen.blit(self.personagem.imagem, (self.personagem.posicaoX, self.personagem.posicaoY))

            tempo_passado = time.time() - inicio
            self.tela.desenharTexto(f"Tempo: {tempo_passado:.2f}s", self.fonte_pequena, (255, 255, 255), 100, 30, self.screen)

            pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(*self.labirinto.posicaoSaida, 50, 50), 2)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.personagem.mover("esquerda")
            if keys[pygame.K_RIGHT]:
                self.personagem.mover("direita")
            if keys[pygame.K_UP]:
                self.personagem.mover("cima")
            if keys[pygame.K_DOWN]:
                self.personagem.mover("baixo")

            personagem_rect = pygame.Rect(self.personagem.posicaoX, self.personagem.posicaoY, 32, 32)
            saida_rect = pygame.Rect(*self.labirinto.posicaoSaida, 50, 50)

            if personagem_rect.colliderect(saida_rect):
                self.estado = "fim"
                self.verificarSaida(tempo_passado)

            self.clock.tick(30)

    def verificarSaida(self, tempo):
        self.tela.exibir(self.screen)
        self.tela.desenharTexto("Você escapou!", self.fonte, (255, 255, 255), 300, 200, self.screen)
        self.tela.desenharTexto(f"Tempo: {tempo:.2f}s", self.fonte_pequena, (255, 255, 255), 300, 250, self.screen)
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
