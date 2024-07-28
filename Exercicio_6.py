# Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: 
# IMC = peso / (altura x altura)

# Solicite ao usuário o peso em Kg e a altura em metros 
peso_usuario = float(input("Digite o seu peso: "))

altura_usuario = float(input("Digite aqui a sua altura: "))

# Calcule o resultado
IMC = peso_usuario / (altura_usuario * altura_usuario)

# Informe os resultados
print(f'O seu Índice de Massa Corporal (IMC) é de {IMC:.0f}.')
