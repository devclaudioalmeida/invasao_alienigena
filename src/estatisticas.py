class EstatisticasJogo:
    """Classe gerenciar as estatísticas do jogo"""
    def __init__(self, ai_jogo):
        """ Inicializa as estatísticas de Invasão Alienígena"""
        self.config = ai_jogo.config
        self.reinicia_estatisticas()

        # Apontuação máxima nunca deve ser redefinida
        self.max_pontos= 0


    def reinicia_estatisticas(self):
        """ Reinicializa as estatísticas que podem mudar durante o jogo"""
        self.naves_restantes = self.config.limite_naves
        self.pontuacao = 0
        self.nivel = 1
    
        