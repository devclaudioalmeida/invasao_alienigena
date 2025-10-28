import pygame
from pygame.sprite import Sprite

class Alienigena (Sprite):
    """ Classe para representar um único alienígena da frota"""
    def __init__(self, ai_jogo):
        super().__init__()
        self.tela = ai_jogo.tela

        #Carrega a imagem do alienígena e defien seu atributo rect
        self.image = pygame.image.load('imagens/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada alienígena novo preto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alienígena
        self.x = float(self.rect.x)

