import json

# Dados do faturamento em formato JSON
faturamento_diario = '''
{
    "01": 12000.00,
    "02": 0.00,
    "03": 15000.00,
    "04": 18000.00,
    "05": 0.00,
    "06": 13000.00,
    "07": 0.00,
    "08": 0.00,
    "09": 16000.00,
    "10": 11000.00,
    "11": 0.00,
    "12": 17000.00
}
'''

faturamento = json.loads(faturamento_diario)

valores = list(faturamento.values())
dias_com_faturamento = [valor for valor in valores if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
menor_faturamento = min(dias_com_faturamento)
maior_faturamento = max(dias_com_faturamento)
dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")