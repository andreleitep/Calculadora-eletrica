from unicodedata import numeric


class un_eltrc:
    '''Unidade Elétrica (equipamento eletro-eletrônico)'''
    def __init__(self, nome, ddp, potencia, corrente):
        '''nome, ddp (Volt), potencia (Watt), corrente (Ampère)'''
        if ddp is not int:
            self.ddp = int(input('digite o valor da tensão elétrica (ddp): '))
        if potencia is not int:

        self.nome = nome
        self.ddp = ddp
        self.potencia = potencia
        self.corrente = corrente

    def calc_gasto_en(self, tempo, custo):
        '''tempo (h) custo (R$) Calcula o gasto de energia (KW) e o valor da conta (R$)'''
        energia = (self.potencia / 1000) * tempo
        custo_total = energia * custo
        return energia, custo_total

    def pot_pela_corrente(self):
        while self.ddp is not int:
            self.ddp = int(input('digite o valor da tensão elétrica (ddp): '))
        self.potencia = self.ddp * self.corrente
        print('potência =', self.potencia, 'watts')