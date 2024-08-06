# Importação do módulo os: O módulo os fornece uma maneira de 
# interagir com o sistema operacional. Aqui, ele é usado para obter o caminho real do arquivo.

import os

# open("dados1.txt", 'w', encoding='utf-8'): Abre o arquivo chamado dados1.txt em modo de escrita ('w'). 
# Se o arquivo não existir, ele será criado. Se o arquivo já existir, seu conteúdo será apagado.
# 'encoding='utf-8': Define a codificação do arquivo como UTF-8, 
# que é uma codificação de texto amplamente utilizada e compatível com a maioria dos caracteres.

arquivo1 = open("dados1.txt", 'w', encoding='utf-8')

# os.path.realpath(arquivo1.name): Obtém o caminho absoluto do arquivo. 

print(os.path.realpath(arquivo1.name)) 

# arquivo1.write("Olá mundo!"): Escreve a string "Olá mundo!" no arquivo.
    
arquivo1.write("Olá mundo!")

print(os.path.realpath(arquivo1.name))

print(arquivo1)

# arquivo1.close(): Fecha o arquivo. Fechar um arquivo é uma boa prática para garantir 
# que todos os dados sejam gravados corretamente e para liberar recursos do sistema associados ao arquivo.

arquivo1.close()

