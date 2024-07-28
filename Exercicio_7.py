# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas por mês. 
# Calcule e mostre o total do seu salário no referido mês. 

# Solicite a entrada de quanto você ganha por hora e o número de horas trabalhadas no mês.

ganha_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas_dia = float(input("Quanto você trabalha por dia? "))
dias_trabalhados_mes = int(input("Quantos dias você trabalhou no mês? "))

# Calcule o sálario do mês

# Calcule o número total de horas trabalhadas no mês
horas_trabalhadas_mes = horas_trabalhadas_dia * dias_trabalhados_mes

# Calcule o salário do mês
salario = ganha_por_hora * horas_trabalhadas_mes


# Informe o resultado

print(f'O seu salário deste mês é de {salario:.2f}')

