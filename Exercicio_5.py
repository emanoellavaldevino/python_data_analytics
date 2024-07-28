# Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus. 
# Levando em consideração: Avião = 600km/h, carro = 100km/h, ônibus = 80km/h

# Entrada de dados
distancia = float(input("Digite aqui o tempo de sua viagem: "))

# Velocidade em km/h

Velocidade_aviao = 600 
Velocidade_carro = 100
Velocidade_onibus = 80

# Calcule o tempo de viagem
tempo_aviao = distancia / Velocidade_aviao
tempo_carro = distancia / Velocidade_carro
tempo_onibus = distancia / Velocidade_onibus 

# Imprima o resultado

print(f'O tempo de viagem de avião foi de {tempo_aviao:.2f}horas, de carro foi de {tempo_carro:.2f}horas e de ônibus {tempo_onibus:.0f}horas.')
