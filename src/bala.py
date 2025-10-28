import pygame
from pygame.sprite import Sprite

class Bala (Sprite):
    """ Classe para gerenciar as balas disparadas da espaçonave"""
    def __init__(self, ai_jogo):
        """ Cria o obeto bala na posição atual da espaçonave"""
        super().__init__()
        self.tela = ai_jogo.tela
        self.config = ai_jogo.config
        self.cor = self.config.cor_bala

        # Cria um bala rect em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, self.config.largura_bala, self.config.altura_bala)
        self.rect.midtop = ai_jogo.nave.rect.midtop

        # Armazena a posição da bala como um float
        self.y = float(self.rect.y)


    def desenha_bala(self):
        """ Desenha a bala na tela"""
        pygame.draw.rect(self.tela, self.cor, self.rect)
        

    def update(self):
        """ Desloca a bala verticalmente pela tela"""
        # Atualiza a posição exata da bala
        self.y -= self.config.velocidade_bala
        #Atualiza a posição do rect
        self.rect.y = self.y

    