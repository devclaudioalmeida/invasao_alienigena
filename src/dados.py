import pygame.font

class DadosJogo:
    """ Classe para exibir informações de pontuação atual, máxima e espaçonaves restantes"""
    def __init__(self, ai_jogo):
        self.tela = ai_jogo.tela
        self.tela_rec = ai_jogo.tela.get_rect()
        self.config = ai_jogo.config
        self.estatisticas = ai_jogo.estatisticas

        # Configuração de fonte para informação de pontuação
        self.cor_texto = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem inicial da pontuação
        self.prepara_pontos()


    def prepara_pontos(self):
        """Transforma a pontuação em uma imagem renderizada"""
        pontos_str = str(self.estatisticas.pontuacao)
        self.pontos_imagem = self.font.render(pontos_str, True, self.cor_texto, self.config.cor_fundo)

        # Exibe a pontuação no canto superior direito da tela
        self.pontos_rect = self.pontos_imagem.get_rect()
        self.pontos_rect.right = self.tela_rec.right - 20
        self.pontos_rect.top = 20

    def mostra_pontos(self):
        """Desenha a pontuação na tela"""
        self.tela.blit(self.pontos_imagem, self.pontos_rect)

        