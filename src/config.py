class Config:
    """Classe para gerenciar as configurações dos componentes do jogo"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        #Configurações da tela
        self.largura_tela = 1400
        self.altura_tela = 900
        self.cor_fundo = (230, 230, 230)
        
        #Configurações da espaçonave
        self.limite_naves = 3

        # Configurações do projétil
        self.largura_bala = 2
        self.altura_bala = 6
        self.cor_bala = (60, 60, 60)
        self.balas_permitidas = 15

        # Configuração do alienígena
        self.velocidade_descida_frota = 10
        
        # A rapidez que o jogo acelera
        self.escala_aumento_velocidade = 1.1
        # Escala para aumentar a pontuação de acordo com que a velocidade do jogo aumenta
        self.escala_aumento_pontuacao = 1.5

        self.incializa_configuracoes_dinamicas()

    def incializa_configuracoes_dinamicas(self):
        """ Inicializa as configurações que mudam ao longo do tempo"""
        self.velocidade_nave = 1.5
        self.velocidade_bala = 2.5
        self.velocidade_alien = 1.0

        # Quando direcao_frota = 1 (movimenta para direita)
        # Quando direcao_frota = -1 (movimenta para esquerda)
        self.direcao_frota = 1

        #Configurações de pontuação
        self.pontos_alien = 10

    def aumenta_velocidade_jogo(self):
        """Aumenta as configurações de velocidade"""
        self.velocidade_alien *= self.escala_aumento_velocidade
        self.velocidade_bala *= self.escala_aumento_velocidade
        self.velocidade_nave *= self.escala_aumento_velocidade
        self.pontos_alien = int(self.pontos_alien * self.escala_aumento_pontuacao)

