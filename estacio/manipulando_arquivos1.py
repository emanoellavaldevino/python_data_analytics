import os

# Open no modo escrita

arquivo = open('dados1.txt', 'r', encoding='utf-8')

# Exibindo os atributos do arquivo
print("Nome do arquivo:", arquivo.name)
print("Modo de abertura:", arquivo.mode)
print("Arquivo está fechado?", arquivo.closed)

# Abrindo o arquivo no modo de escrita
arquivo = open('dados1.txt', 'w', encoding='utf-8')

# Escrevendo no arquivo
arquivo.write("Olá, Emanoella!")

# Arquivo no modo de leitura para verificar o conteúdo
arquivo = open('dados1.txt', 'r', encoding='utf-8')

# Lendo e imprimindo o conteúdo do arquivo
conteudo = arquivo.read()
print("Conteúdo do arquivo:", conteudo)

# Fechando o arquivo para escrita e leitura
arquivo.close()

# Verificando se o arquivo foi fechado corretamente
print("Arquivo está fechado?", arquivo.closed)

