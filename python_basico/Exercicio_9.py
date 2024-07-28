# Faça um programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. 
# Exemplos de variáveis: nome, idade, lugar, profissão. 
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área. 

# Solicite ao usuário o seu nome, idade, lugar, profissão. 

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
lugar = input("Onde você nasceu? ")
profissao = input("Qual é a sua profissão? ")

print(f'Olá {nome}, prazer em te conhecer! Sou de {lugar} também.')
print(f'Estou migrando de área para {profissao}. É inspirador ver que mesmo com {idade} anos, muitas pessoas estão fazendo essa mudança.')
