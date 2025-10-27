import pygame, sys

from config import Config
from espaconave import Nave

class InvasaoAlien:
    def __init__(self):
        """Inicializa o jogo e cria os recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.config = Config()

        self.tela = pygame.display.set_mode((self.config.largura_tela, self.config.altura_tela))
        pygame.display.set_caption("Invasão Alien")
        self.nave = Nave(self)

        #Define a cor do background
    
    def _checa_eventos(self):
        #observa os eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #move a espaçonave para a direita
                        self.nave.movendo_direita = True
                    elif event.key == pygame.K_LEFT:
                        #Move a espaçonave para a esquerda
                        self.nave.movendo_esquerda = True
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        #move a espaçonave para a direita
                        self.nave.movendo_direita = False
                    elif event.key == pygame.K_LEFT:
                        #Move a espaçonave para a esquerda
                        self.nave.movendo_esquerda = False

    
    def _atualiza_tela(self):
        #Redesenha a tela durante cada passagem pelo loop
        self.tela.fill(self.config.cor_fundo)
        self.nave.blitme()
            
        #Deixa a tela desenhada mais recente visível
        pygame.display.flip()
    
    
    def executa_jogo(self):
        """Inicia o loop principal do jogo"""
        while True:

            self._checa_eventos()
            self.nave.atualiza()
            self._atualiza_tela()
            self.clock.tick(60)

    

if __name__ == '__main__':
    #Cria a instancia do jogo e executa o jogo
    ai = InvasaoAlien()
    ai.executa_jogo()
    