# Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros. 

# Solicita a quilometragem do usuário

num1 = float(input("Qual é a quilometragem?  "))

# Transformando os resultados

metros = num1 * 1000
centimetros = num1 * 100000
milimetros = num1 * 1000000

# Imprimindo os resultados

# Colocar :.0f para garantir que o número seja exibido como um número inteiro.

print(f'O resultado em metros é {metros:.0f}, em centimetros é {centimetros:.0f}, em milimetros é {milimetros:.0f}.')

