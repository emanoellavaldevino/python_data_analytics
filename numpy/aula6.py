import numpy as np

# Seleciona as primeiras 3 linhas da matriz cartela_bingo
# Seleciona a última linha da matriz cartela_bingo usando indexação negativa
# Concatena as duas matrizes (cartela_bingo1 e cartela_bingo2) verticalmente

'''
cartela_bingo = np.array([[2, 22, 31, 18],
                         [24, 5, 17, 25],
                         [39, 6, 21, 32],
                         [89, 8, 78, 19]])

cartela_bingo1 = cartela_bingo[:3]
cartela_bingo2 = cartela_bingo[-1:]
print(cartela_bingo1)

print(f' Segundo print {cartela_bingo2}')

cartela_bingo_volta = np.concatenate((cartela_bingo1, cartela_bingo2))
print(f'Terceiro print {cartela_bingo_volta}') '''

# Deletando a última array, horizontal
'''
sala_espera = np.array([['5', '30', '1', 'Luzinete'],
                        ['6', '29', '1', 'Luana'],
                        ['7', '35', '3', 'Mariana'],
                        ['8', '34', '3', 'Danielle']])

deletando = np.delete(sala_espera, 3, axis=0)
print(deletando) '''

# 1. Adicione mais 2 espécies ao array[[204, 10, 40, 12], [392, 11, 81, 11]]
# 2. Adicione mais uma coluna na no array original agora com o número de espécies encontradas
# com que indica se o animal enxerga ou não: [0, 1, 0, 0, 0, 0, 1, 1, 0, 1]
# 3. Faça um array com todas as espécies menos as com ID: 623, 116, 613 

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

''' novas_especies = np.array([[204, 10, 40, 12], [392, 11, 81, 11]])
adicionando = np.concatenate((especie, novas_especies), axis=0)
print(adicionando) ''' # Exercício 1

# Adiciona a nova coluna ao array original
'''nova_especies = np.array([0, 1, 0, 0, 0, 0, 1, 1, 0, 1])
adicionando = np.concatenate((especie, nova_especies.reshape(-1, 1)), axis=1)
print(adicionando) '''

# IDs a serem excluídos
ids_excluir = [623, 116, 613]

mask = (especie[:, 0] != ids_excluir[0]) & (especie[:, 0] 
!= ids_excluir[1]) & (especie[:, 0] != ids_excluir[2])
especie_filtrada = especie[mask]


print(especie_filtrada)







