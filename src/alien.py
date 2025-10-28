import pygame
from pygame.sprite import Sprite

class Alienigena (Sprite):
    """ Classe para representar um único alienígena da frota"""
    def __init__(self, ai_jogo):
        super().__init__()
        self.tela = ai_jogo.tela
        self.config = ai_jogo.config

        #Carrega a imagem do alienígena e defien seu atributo rect
        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada alienígena novo preto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alienígena
        self.x = float(self.rect.x)


    def checa_bordas(self):
        """Retorna True se o alienígena chegar a borda da tela"""
        tela_rect = self.tela.get_rect()
        return (self.rect.right >= tela_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move o alienígena para a direita ou esquerda"""
        self.x += self.config.velocidade_alien * self.config.direcao_frota
        self.rect.x = self.x
        

