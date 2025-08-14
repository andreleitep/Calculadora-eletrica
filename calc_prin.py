from classes import UnEltrc, hora_to_decimal

print(hora_to_decimal(input('horas: ')))

'''
entrada = input('Digite o nome, ddp (Volt), potencia (Watt), corrente (Ampère) do aparelho (separados por espaço): ')
atributos = entrada.split()
aparelho = UnEltrc(atributos[0], atributos[1], atributos[2], atributos[3])
entrada = input('Digite quanto tempo (h) de uso e o valor do KW/h na sua região (separados por espaço): ')
tempo_custo = entrada.split()
ener_gasta, custo_tot = aparelho.calc_gasto_en(float(tempo_custo[0]), float(tempo_custo[1]))
print(f'energia gasta pelo aparelho {aparelho.nome} = {ener_gasta}KW em {tempo_custo[0]} horas')
print(f'custo total gerado pelo aparelho {aparelho.nome} = R$ {custo_tot:.2f}')
'''