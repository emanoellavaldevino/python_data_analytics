# Receba do usuário a quantidade de litros de combustível e a distância percorrida. Calcule e imprima o consumo médio em km/l.

# Solicita a quantidade de combustível

combustivel = float(input("Qual é a quantidade de combustível? "))

# Solicita a distância percorrida

distancia = float(input("Qual é a distância percorrida? "))

# Calcule o consumo médio

consumo_medio = distancia / combustivel

# Imprima o resultado

print(f'O consumo médio é de {consumo_medio:.2f} km/l.')
