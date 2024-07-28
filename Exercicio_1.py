# Exercícios de conceito básicos de Python

# Faça um programa que peça dois números, realize as principais operações: soma, subtração, multiplicação e divisão.

# Solicita os números ao usuário

numero = float(input("Digite o seu primeiro número: "))
numero2 = float(input("Digite o seu segundo número: "))

# Realiza as operações básicas

soma = numero + numero2
sub = numero - numero2
multi = numero * numero2
div = numero / numero2

# Exibe os resultados

print(f"O total dos dois números somados é de {soma}.")
print(f"O total dos dois números subtraidos é de {sub}.")
print(f"O total dos dois números multiplicados é de {multi}.")
print(f"O total dos dois números divididos é de {div}.")
