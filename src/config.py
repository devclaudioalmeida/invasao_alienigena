class Config:
    def __init__(self):
        """Inicializa as configurações do jogo"""
        #Configurações da tela
        self.largura_tela = 1200
        self.altura_tela = 800
        self.cor_fundo = (230, 230, 230)
        
        #Configurações da espaçonave
        self.velocidade_nave = 1.5

        # Configurações do projétil
        self.velocidade_bala = 2.0
        self.largura_bala = 3
        self.altura_bala = 10
        self.cor_bala = (60, 90, 60)
        self.balas_permitidas = 5