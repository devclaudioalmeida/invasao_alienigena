import pygame

class Nave:
    def __init__(self, ai_jogo):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.tela = ai_jogo.tela
        self.tela_rect = ai_jogo.tela.get_rect()

        #Sobe a imagem da espaçonave e obtem seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        #Começa a espaçonave no centro inferior da tela
        self.rect.midbottom = self.tela_rect.midbottom

        #Flags de movimento; começa com uma espaçonave que não está se movendo
        self.movendo_esquerda = False
        self.movendo_direita = False

    def atualiza(self):
        """Atualiza a posição da espaçonave com base nas flags de movimento"""
        if self.movendo_direita:
            self.rect.x += 1
        elif self.movendo_esquerda:
            self.rect.x -= 1

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.tela.blit(self.image, self.rect)