import pygame, sys

from time import sleep

from config import Config
from espaconave import Nave
from bala import Bala
from alien import Alienigena
from estatisticas import EstatisticasJogo
from botao import Botao

class InvasaoAlien:
    """Classe principal do jogo"""
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
        self.estatisticas = EstatisticasJogo(self)
        self.nave = Nave(self)
        self.balas = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._cria_frota_alien()

        # Inicializa Invasão Alienigena com um estado ativo
        self.jogo_ativo = False

        #Cria o botão play
        self.botao_play = Botao(self, "JOGAR")


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

    
    def _clicou_botao_play(self, posicao):
        clicou_botao = self.botao_play.rect.collidepoint(posicao)
        if clicou_botao and not self.jogo_ativo:
            self.estatisticas.reinicia_estatisticas()
            self.jogo_ativo = True
        
            #Descarta as balas e oa alienígenas restantes
            self.balas.empty()
            self.aliens.empty()

            #Cria uma nova frota de alienígenas e centraliza a nave
            self._cria_frota_alien()
            self.nave.centraliza_nave()


    def _checa_eventos(self):
        # Observa os eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._checa_keydown_eventos(event)
                
                elif event.type == pygame.KEYUP:
                    self._checa_keyup_eventos(event)

                #Verifica clique de botão esquerdo do mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posicao_mouse = pygame.mouse.get_pos()
                    self._clicou_botao_play(posicao_mouse)



    def _dispara_bala(self):
        """ 
        Cria uma nova bala e adiciona ao grupo de balas caso o numero de balas na tela seja menor que
        o número de balas permitidas em config
        """
        if len(self.balas) < self.config.balas_permitidas:
            nova_bala = Bala(self)
            self.balas.add(nova_bala)

    def _verifica_colisao_bala_alien(self):
        #Verifica se alguma bala atingiu algum alienígena
        #Se sim descarta a bala e o alienígena
        colisoes = pygame.sprite.groupcollide(self.balas, self.aliens, True, True)
        if not self.aliens:
            # Destroi os projeteis existentes e cria uma frota de alienigenas nova
            self.balas.empty()
            self._cria_frota_alien()


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

        # Se alguma bala atingir algum alienígena eleimina ambos
        self._verifica_colisao_bala_alien()
    

    def _nave_bateu(self):
        """ Responde à espaçonave sendo abatida por um alienígena"""
        if self.estatisticas.naves_restantes > 0:
            # Diminue uma espaçonave restante
            self.estatisticas.naves_restantes -= 1

            # Descarta balas e alienígenas restantes
            self.balas.empty()
            self.aliens.empty()

            # Cria uma frota nova de alienígenas e centraliza a espaçonave
            self._cria_frota_alien()
            self.nave.centraliza_nave()

            # Pausa de meio segundo
            sleep(0.5)
        else:
            self.jogo_ativo = False

    
    def _verifica_alien_embaixo(self):
        """ Verifica se algum alienígena chegou a parte inferior da tela"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.config.altura_tela:
                # Trata isso como se a espaçonave tivesso batido
                self._nave_bateu()
                break


    def _atualiza_aliens(self):
        """Verifica se tem algum alienígena na borda, em seguida atualiza as posiçoes"""
        self._verifica_alien_na_borda()
        self.aliens.update()

        # Detecta colisões entre alienigenas e espaçonaves
        if pygame.sprite.spritecollideany(self.nave, self.aliens):
            self._nave_bateu()
            #print('A nave bateu!')
        
        # Verifica se algum alienígena chegou a parte inferior da tela
        self._verifica_alien_embaixo()


    def _cria_alien(self, pos_horizontal, pos_vertical):
        """ Cria um alienígena e posiciona na fileira"""
        novo_alien = Alienigena(self)
        novo_alien.x = pos_horizontal
        novo_alien.rect.x = pos_horizontal
        novo_alien.rect.y = pos_vertical
        self.aliens.add(novo_alien)
    

    def _verifica_alien_na_borda(self):
        """Responde apropriandamente se algum alinenpigena alcançou alguma borda"""
        for alien in self.aliens.sprites():
            if alien.checa_bordas():
                self._muda_direcao_frota()
                break
    
    
    def _muda_direcao_frota(self):
        """Faz toda a frota descer e mudar de diração"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.config.velocidade_descida_frota
        self.config.direcao_frota *= -1


    def _cria_frota_alien(self):
        """ Cria uma frota de alienígenas"""
        # Cria um alienígena e continua adicionando alienígenas
        # até que não haja mais espaço
        # O distanciamento entre alienígenas é a largura de um alienígena
        alien = Alienigena(self)
        #Aqui pegmos a largura e a altura do alien através do rect.size
        largura_alien, altura_alien = alien.rect.size
        #Aqui passamos as coordenadas iniciais x e y do alienígena
        x_atual = largura_alien
        y_atual = 2 * altura_alien
        while y_atual < (self.config.altura_tela - 5 * altura_alien):
            while x_atual < (self.config.largura_tela - 2 * largura_alien):
                self._cria_alien(x_atual, y_atual)
                x_atual +=  2 * largura_alien
            # Termina a fileira, reinicia o valor de x e incrementa o valor de y
            x_atual = largura_alien
            y_atual += 2 * altura_alien

    
    def _atualiza_tela(self):
        #Redesenha a tela durante cada passagem pelo loop
        #Define a cor do background
        self.tela.fill(self.config.cor_fundo)
        for bala in self.balas.sprites():
            bala.desenha_bala()
        self.nave.desenha_nave()
        self.aliens.draw(self.tela)

        #Desenha o botão Play se o jogo estiver inativo
        if not self.jogo_ativo:
            self.botao_play.desenha_botao()
            
        #Deixa a tela desenhada mais recente visível
        pygame.display.flip()
    
    
    def executa_jogo(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._checa_eventos()
            # Caso as espaçonaves acabem, o jogo congela
            if self.jogo_ativo:
                self.nave.atualiza_nave()
                self._atualiza_balas()
                self._atualiza_aliens()
            
            self._atualiza_tela()
            self.clock.tick(60)

    

if __name__ == '__main__':
    #Cria a instancia do jogo e executa
    ai = InvasaoAlien()
    ai.executa_jogo()
    