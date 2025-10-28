import pygame.font

class Botao():
    def __init__(self, ai_jogo, msg):
        """ Inicializa os atributos do botão"""
        self.tela = ai_jogo.tela
        self.tela_rect = ai_jogo.tela.get_rect()

        # Define as dimensões e propriedades do botão
        self.largura = 200
        self.altura = 50
        self.cor_botao = (0, 135, 0)
        self.cor_texto = (255, 255, 255)
        self.fonte = pygame.font.SysFont(None, 48)

        # Cria o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center = self.tela_rect.center

        # A mensagem do botão precisa ser preparanda apena uma vez
        self._prepara_mensagem(msg)

    def _prepara_mensagem(self, msg):
        """Transforma msg em uma imagem renderizada e centraliza texto no botão"""
        self.msg_imagem = self.fonte.render(msg, True, self.cor_texto, self.cor_botao)
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.center = self.rect.center

    def desenha_botao(self):
        """ Desenha o botão em branco e depois desenha a mensagem"""
        self.tela.fill(self.cor_botao, self.rect)
        self.tela.blit(self.msg_imagem, self.msg_imagem_rect)

        