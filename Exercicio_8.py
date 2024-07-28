# Solicite ao usuário o número de horas de exercício por semana. Calcule o total de calorias queimadas em um mês, considerando
# uma média de 5 calorias por minuto de exercício.

# Solite o usuário o número de horas de exercício por semana

numero_de_horas = float(input("Quantas horas de exercício por semana você faz? "))

# Média de calorias queimadas por minuto

media_por_minuto = 5

# Converta o número de horas por minuto

minutos_por_semana = numero_de_horas * 60

# Calcule o número total de calorias queimadas em uma semana

calorias_queimadas_semana = media_por_minuto * minutos_por_semana

# Calcule o número total de calorias queimadas em um mês (4 semanas) 

calorias_queimadas_mes = calorias_queimadas_semana * 4

# Imprima o resultado

print(f'O número de calórias queimadas no mês foi de {calorias_queimadas_mes:.2f}.')
