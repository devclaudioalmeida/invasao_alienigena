class Config:
    """Classe para gerenciar as configurações dos componentes do jogo"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        #Configurações da tela
        self.largura_tela = 1400
        self.altura_tela = 900
        self.cor_fundo = (230, 230, 230)
        
        #Configurações da espaçonave
        self.velocidade_nave = 1.5
        self.limite_naves = 3

        # Configurações do projétil
        self.velocidade_bala = 2.5
        self.largura_bala = 3
        self.altura_bala = 8
        self.cor_bala = (60, 60, 60)
        self.balas_permitidas = 5

        # Configuração do alienígena
        self.velocidade_alien = 1.0
        self.velocidade_descida_frota = 10
        #direcao_frota = 1 (movimenta para direita)
        #direcao_frota = -1 (movimenta para esquerda)
        self.direcao_frota = 1