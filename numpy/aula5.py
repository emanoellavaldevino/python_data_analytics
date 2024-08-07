import numpy as np

#  verifica se cada elemento de arr1 é divisível por 2 (ou seja, se é par). 
'''
arr1 = np.array([1, 2, 3, 4, 5])
mask = arr1 % 2 == 0
print(mask)'''

# Criar uma máscara para identificar pessoas com idade maior que 21
# Aplicar a máscara para selecionar apenas as linhas onde a idade é maior que 21
'''
pessoas_id_idade = np.array([[1, 22], 
                             [2, 21], 
                             [3, 27], 
                            [4, 26]])

maior = pessoas_id_idade[:, 1] > 21
print(maior)

mask = pessoas_id_idade[maior]
print(mask)

mask1 = np.where(maior)
print(mask1) '''

# Utiliza a função np.where para substituir os elementos da matriz
# Neste caso, se um elemento de cartela_bingo for divisível por 3, 
# ele é substituído pela string 'div3'; caso contrário, o próprio elemento original é mantido.
'''
cartela_bingo = np.array([[2, 22, 31, 18],
                        [24, 5, 17, 25],
                        [39, 6, 21, 32],
                        [89, 8, 78, 19]])

ar1 = np.where(cartela_bingo % 3 == 0, 'div3', cartela_bingo)
print(ar1)'''

# ID da espécie, quantidade de representante encontrados, profundeza, tamanho médio da espécie
# 1. Usando um index booleano crie um array que contém os dados maior espécie encontrada ( considerando seu tamanho)
# esse valor corresponde ao valor 22 
# 2. Usando fency index faça um array que contém apenas dados da espécie com ID 297
# 3. Usando np.where() faça um array com a linha com dados correspondentes a espécie com 105 representantes encontrados
# 4. Considere a profundeza em que a espécie foi encontrada substitua valores maiores que 60 com "profundo"

especie = np.array([[747, 89, 33, 5],
                    [623, 123, 32, 13],
                    [501, 22, 49,  2],
                    [116,  101, 42, 10],
                    [297, 56, 69, 22],
                    [613, 64, 27, 7],
                    [295, 84, 29, 14],
                    [692, 105, 72, 16],
                    [229, 103, 35, 5],
                    [374, 124, 70, 1]])

''' maior = especie[especie[:, 3] == 22]
print(maior)  ''' # Exercicio 1

''' mask_297 = especie[:, 0] == 297
especies_297 = especie[mask_297]
print(especies_297)  '''  # Exercicio 2

''' indice_105 = np.where(especie[:, 1] == 105) 

dados_105 = especie[indice_105]
print(dados_105) ''' # Exercicio 3

profundeza = np.where(especie[:, 2] < 60, "profundo", especie[:, 2])
print(profundeza) # Exercicio 4









