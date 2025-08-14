def hora_to_decimal(hora):
    nao_numericos = [i for i in hora if not i.isdigit()]
    while len(nao_numericos) > 1:
        hora = input('Digite um formato válido de hora: ')
        nao_numericos = [i for i in hora if not i.isdigit()]
    if len(nao_numericos) == 0:
        hr, min = int(hora), 0
    else:

        hr_min = hora.split(nao_numericos[0])
        if not hr_min[0]:
            hr_min[0] = 0
        if hr_min[1] and 0 <= int(hr_min[1]) < 60:
            hr = int(hr_min[0])
            min = int(hr_min[1])
        else:
            hr = int(hr_min[0])
            min = 0



    return hr, min


class UnEltrc:
    '''Unidade Elétrica (equipamento eletro-eletrônico)'''
    def __init__(self, nome, ddp, potencia, corrente):
        '''nome, ddp (Volt), potencia (Watt), corrente (Ampère)'''
        while type(ddp) is not int:
            try:
                ddp = int(ddp)
            except ValueError:
                ddp = input('ddp deve ser um número inteiro (se seu aparelho é bivolt, escolha a tensão da tomada que você usa para ligá-lo): ')
        while type(potencia) is not int:
            try:
                potencia = int(potencia)
            except ValueError:
                potencia = int(input(f'Potência tem que receber um valor numérico inteiro: '))
        while type(corrente) is not int:
            try:
                corrente = int(corrente)
            except ValueError:
                corrente = int(input(f'Corrente tem que receber um valor numérico inteiro: '))

        self.nome = nome
        self.ddp = ddp
        self.potencia = potencia
        self.corrente = corrente

    def calc_gasto_en(self, tempo, custo):
        '''tempo (h) custo (R$) Calcula o gasto de energia (KW) e o valor da conta (R$)'''
        while type(tempo) != float:
            try:
                tempo = float(tempo)
            except ValueError:
                tempo = input('Valor do tempo em horas (apenas números): ')
        while type(custo) != float:
            try:
                custo = float(custo)
            except ValueError:
                custo = input('Valor do custo em reais (apenas números): ')

        energia = (self.potencia / 1000) * tempo
        custo_total = energia * custo
        return energia, custo_total

    def pot_pela_corrente(self):
        self.potencia = self.ddp * self.corrente
        print('potência =', self.potencia, 'watts')