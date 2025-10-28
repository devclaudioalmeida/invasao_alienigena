import pygame

class Nave:
    """Classe para gerenciar espaçonaves"""
    def __init__(self, ai_jogo):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.tela = ai_jogo.tela
        self.config = ai_jogo.config
        self.tela_rect = ai_jogo.tela.get_rect()

        #Sobe a imagem da espaçonave e obtem seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()

        #Começa a espaçonave no centro inferior da tela
        self.rect.midbottom = self.tela_rect.midbottom

        #armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)
        #armazena um float para a posição vertical exata da espaçonave
        self.y = float(self.rect.y)

        #Flags de movimento; começa com uma espaçonave que não está se movendo
        self.movendo_esquerda = False
        self.movendo_direita = False
        self.movendo_acima = False
        self.movendo_abaixo = False


    def atualiza(self):
        """Atualiza a posição da espaçonave com base nas flags de movimento"""
        if self.movendo_direita and (self.rect.right < self.tela_rect.right):
            self.x += self.config.velocidade_nave
        if self.movendo_esquerda and (self.rect.left > 0):
            self.x -= self.config.velocidade_nave
        if self.movendo_abaixo and (self.rect.bottom < self.tela_rect.bottom):
            self.y += self.config.velocidade_nave
        if self.movendo_acima and (self.rect.top > 0):
            self.y -= self.config.velocidade_nave
        
        #atualiza o objeto rect de self.x
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.tela.blit(self.image, self.rect)

    
    def centraliza_nave(self):
        self.rect.midbottom = self.tela_rect.midbottom
        self.x = float(self.rect.x)