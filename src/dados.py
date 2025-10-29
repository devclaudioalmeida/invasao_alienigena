import pygame.font
from pygame.sprite import Group

from src.espaconave import Nave

class DadosJogo:
    """ Classe para exibir informações de pontuação atual, máxima e espaçonaves restantes"""
    def __init__(self, ai_jogo):
        self.ai_jogo = ai_jogo
        self.tela = ai_jogo.tela
        self.tela_rect = ai_jogo.tela.get_rect()
        self.config = ai_jogo.config
        self.estatisticas = ai_jogo.estatisticas

        # Configuração de fonte para informação de pontuação
        self.cor_texto = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem inicial da pontuação
        self.prepara_pontos()
        self.prepara_pontuação_maxima()
        self.prepara_nivel()
        self.prepara_naves()
   

    def prepara_pontos(self):
        """Transforma a pontuação em uma imagem renderizada"""
        pontos_arredondados = round(self.estatisticas.pontuacao, -1)
        pontos_str = f'{pontos_arredondados:,}'
        self.pontos_imagem = self.font.render(pontos_str, True, self.cor_texto, self.config.cor_fundo)

        # Exibe a pontuação no canto superior direito da tela
        self.pontos_rect = self.pontos_imagem.get_rect()
        self.pontos_rect.right = self.tela_rect.right - 20
        self.pontos_rect.top = 20

    
    def prepara_pontuação_maxima(self):
        """Transforma a pontuação máxima em uma imagem renderizada"""
        max_pontos = round(self.estatisticas.max_pontos, -1)
        max_pontos_str = f'RECORDE {max_pontos:,}'
        self.max_pontos_imagem = self.font.render(max_pontos_str, True, self.cor_texto, self.config.cor_fundo)

        # Centraliza a pontuação máxima do jogo
        self.max_pontos_rect = self.max_pontos_imagem.get_rect()
        self.max_pontos_rect.center = self.tela_rect.center
        self.max_pontos_rect.top = self.pontos_rect.top
    

    def prepara_nivel(self):
        """Transforma o numero do nível em uma imagem renderizada"""
        nivel_str = str(f'NÍVEL {self.estatisticas.nivel}')
        self.nivel_amgem = self.font.render(nivel_str, True, self.cor_texto, self.config.cor_fundo)

        # Exibe o nível no lado direito abaixo da pontuação atual
        self.nivel_rect = self.nivel_amgem.get_rect()
        self.nivel_rect.right = self.tela_rect.right - 20
        self.nivel_rect.top = self.pontos_rect.bottom + 10


    def prepara_naves(self):
        """Mostra as espaçonaves restantes"""
        self.naves = Group()
        for nave_numero in range(self.estatisticas.naves_restantes):
            nave = Nave(self.ai_jogo)
            nave.rect.x = 10 + nave_numero * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)

    
    def checa_pontuacao_maxima(self):
        """Verifica se há uma nova pontuação máxima"""
        if self.estatisticas.pontuacao > self.estatisticas.max_pontos:
            self.estatisticas.max_pontos = self.estatisticas.pontuacao
            self.prepara_pontuação_maxima()


    def mostra_pontos(self):
        """Desenha as pontuações, o nível e as espaçonaves restantes na tela"""
        self.tela.blit(self.pontos_imagem, self.pontos_rect)
        self.tela.blit(self.max_pontos_imagem, self.max_pontos_rect)
        self.tela.blit(self.nivel_amgem, self.nivel_rect)
        self.naves.draw(self.tela)

        