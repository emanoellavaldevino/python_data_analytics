import numpy as np

#  Um array NumPy de uma dimensão (1D) contendo os elementos 
'''
a1 = np.array([1, 22, 24, 37])
print(a1[1])'''


# Definindo a cartela de bingo
# Selecionando a segunda coluna
# Reformatando a segunda coluna para um array 2D com 4 linhas e 1 coluna
'''
cartela_bingo = np.array([[2, 22, 31, 18],
                        [24, 5, 17, 25],
                        [39, 6, 21, 32],
                        [89, 8, 78, 19]])

segunda_coluna = cartela_bingo[:, 1]

segunda_coluna_reshaped  = segunda_coluna.reshape(-1, 1)

print(segunda_coluna_reshaped)'''

# np.sort: Ela deixa organizado em ordem vertical
'''
cartela_bingo = np.sort([[2, 22, 31, 18],
                        [24, 5, 17, 25],
                        [39, 6, 21, 32],
                        [89, 8, 78, 19]])

print(cartela_bingo) '''

# Ordenando a cartela de bingo ao longo do eixo 0 (colunas)
'''
cartela_bingo = np.sort([[2, 22, 31, 18],
                        [24, 5, 17, 25],
                        [39, 6, 21, 32],
                        [89, 8, 78, 19]])

cartela_bingo_ordenada = np.sort(cartela_bingo, axis=0)
print(cartela_bingo_ordenada) '''

# Selecione a segunda coluna com a quantidade de espécie encontradas e adicione em um array como "qt_especies"
# ID da espécie, quantidade de representante encontrados, profundeza, tamanho médio da espécie
'''
especie = np.random.randint(1, 751, size=(10, 4))
print(especie)'''

''' especie = np.array([[368, 433, 471, 426],
                    [349, 558, 136, 383],
                    [692, 485, 382,  31],
                    [ 57,  67, 365, 224],
                    [243, 578, 574, 156],
                    [528, 60, 290, 641],
                    [307, 251, 380, 106],
                    [440, 217, 697, 572],
                    [561, 129, 595, 614],
                    [675, 600, 666, 332]])

qt_especies = especie[:, 1]
print(qt_especies) '''

# De qt_especie selecione apenas as primeiras 3 quantidades e print
# Selecionando a segunda coluna
''' 
especie = np.array([[368, 433, 471, 426],
                    [349, 558, 136, 383],
                    [692, 485, 382,  31],
                    [ 57,  67, 365, 224],
                    [243, 578, 574, 156],
                    [528, 60, 290, 641],
                    [307, 251, 380, 106],
                    [440, 217, 697, 572],
                    [561, 129, 595, 614],
                    [675, 600, 666, 332]])

qt_especies = especie[:, 1]
primeiras_tres_qt = qt_especies[:3]
print(primeiras_tres_qt) '''

# Print as 5 últimas quantidades de espécies
'''
especie = np.array([[368, 433, 471, 426],
                    [349, 558, 136, 383],
                    [692, 485, 382,  31],
                    [ 57,  67, 365, 224],
                    [243, 578, 574, 156],
                    [528, 60, 290, 641],
                    [307, 251, 380, 106],
                    [440, 217, 697, 572],
                    [561, 129, 595, 614],
                    [675, 600, 666, 332]])

qt_especie = especie[:, 0]
cinco_ultimas = qt_especie[-5:]
print(cinco_ultimas)'''

# Crie um array que contenha apenas os tamanhos das especies e ordene por ordem crescente
# Descrescente [::-1]
# Crescente np.sort 

especie = np.array([[368, 433, 471, 426],
                    [349, 558, 136, 383],
                    [692, 485, 382,  31],
                    [ 57,  67, 365, 224],
                    [243, 578, 574, 156],
                    [528, 60, 290, 641],
                    [307, 251, 380, 106],
                    [440, 217, 697, 572],
                    [561, 129, 595, 614],
                    [675, 600, 666, 332]])

tamanho_especie = especie[:, 3]
ordem_crescente = np.sort(tamanho_especie)
print(ordem_crescente)

