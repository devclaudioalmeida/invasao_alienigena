import pygame, sys

from config import Config
from espaconave import Nave
from bala import Bala

class InvasaoAlien:
    def __init__(self):
        """Inicializa o jogo e cria os recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.config = Config()

        #Tamanho de tela padrão
        self.tela = pygame.display.set_mode((self.config.largura_tela, self.config.altura_tela))

        #tela Cheia
        #self.tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.config.largura_tela = self.tela.get_rect().width
        #self.config.altura_tela = self.tela.get_rect().height

        pygame.display.set_caption("Invasão Alien")
        self.nave = Nave(self)
        self.balas = pygame.sprite.Group()


    def _checa_keydown_eventos(self,event):
        if event.key == pygame.K_RIGHT:
            # Habilita o movimento da espaçonave para a direita
            self.nave.movendo_direita = True
        elif event.key == pygame.K_LEFT:
            # Habilita o movimento da espaçonave para a esquerda
            self.nave.movendo_esquerda = True
        #elif event.key == pygame.K_UP:
            # Habilita o movimento da espaçonave para cima
            #self.nave.movendo_acima = True
        #elif event.key == pygame.K_DOWN:
            # Habilita o movimento da espaçonave para baixo
            #self.nave.movendo_abaixo = True

        elif event.key == pygame.K_SPACE:
            # dispara uma bala cada vez que pressonar a tecla "ESPAÇO"
            self._dispara_bala()
                
        elif event.key == pygame.K_ESCAPE:
            # Exerra o jogo quando pressiona a técla "ESC"
            sys.exit()


    def _checa_keyup_eventos(self,event):
        if event.key == pygame.K_RIGHT:
            # Desabilita o movimento da espaçonave para a direita
            self.nave.movendo_direita = False
        elif event.key == pygame.K_LEFT:
            # Desabilita o movimento da espaçonave para a esquerda
            self.nave.movendo_esquerda = False
        elif event.key == pygame.K_UP:
            # Desabilita o movimento da espaçonave para a direita
            self.nave.movendo_acima = False
        elif event.key == pygame.K_DOWN:
            # Desabilita o movimento da espaçonave para a esquerda
            self.nave.movendo_abaixo = False


    def _checa_eventos(self):
        # Observa os eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._checa_keydown_eventos(event)
                
                elif event.type == pygame.KEYUP:
                    self._checa_keyup_eventos(event)


    def _dispara_bala(self):
        """ 
        Cria uma nova bala e adiciona ao grupo de balas caso o numero de balas na tela seja menor que
        o número de balas permitidas em config
        """
        if len(self.balas) < self.config.balas_permitidas:
            nova_bala = Bala(self)
            self.balas.add(nova_bala)


    def _atualiza_balas(self):
        """ Atualiza a posição das balas e descarta as antigas"""
        #Atualiza a posição das balas
        self.balas.update()

        #Descarta os projeteis que desaparecemna tela
        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)
        #Somente para verificação, pode remover
        #print(len(self.balas))

    
    def _atualiza_tela(self):
        #Redesenha a tela durante cada passagem pelo loop
        #Define a cor do background
        self.tela.fill(self.config.cor_fundo)
        for bala in self.balas.sprites():
            bala.desenha_bala()
        self.nave.blitme()
            
        #Deixa a tela desenhada mais recente visível
        pygame.display.flip()
    
    
    def executa_jogo(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._checa_eventos()
            self.nave.atualiza()
            self._atualiza_balas()
            self._atualiza_tela()
            self.clock.tick(60)

    

if __name__ == '__main__':
    #Cria a instancia do jogo e executa o jogo
    ai = InvasaoAlien()
    ai.executa_jogo()
    