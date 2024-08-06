import numpy as np

# ar.shape: Este atributo retorna a forma do array ' ar ' como uma tupla. 
# Neste exemplo, ele retornará (2, 4), indicando que o array tem 2 linhas e 4 colunas.
'''
ar =  np.zeros((2,4))

print(ar.shape)'''

#  Combina os três arrays 2x2 em um array tridimensional.
'''
arra1 = np.array([[1,2], [3,4]])
arra2 = np.array([[5,6], [4,5]])
arra3 = np.array([[8,3], [2,7]])

array = np.array([arra1, arra2, arra3])

print(array) '''

# Cria um array tridimensional (3D) de zeros com a forma (3, 4, 2). 
# (3, 4, 2). 3 blocos, 4 linhas de cada bloco e 2 colunas
# arr.shape: Obtém a forma do array arr, que é uma tupla indicando as dimensões do array.
''' 
arr = np.zeros((3,4,2))

arr.shape ou print(arr.shape) '''

# O método Flatten do Numpy é usado para transformar uma array multidimensional em um array unidimensional(1D)
# Ele retona uma cópia de array colapsado em uma única dimensão 
'''
arra1 = np.array([[1,2], [3,4]])
arra2 = np.array([[5,6], [4,5]])

array = np.array([arra1, arra2,])
print(array.flatten()) '''

# O método reshape ele reorganiza os elementos na nova forma. O número total permanece o mesmo, porque ele não cria ou destrói dados
# Apenas altera a estrutura de como os dados são visualizados
'''
arra3 = np.array([[2,3], [2,7]])
reshaped_array = arra3.reshape(4,1)

print(reshaped_array) '''

# Reduza o array (5,7) a apenas uma dimensão
'''
exer1 = np.random.random((5,7)) 
print(exer1.flatten())'''

# Considerando que você é organizadora de um jogo Bingo. Crie uma Array que irá representar a cartilha de jogos de bingo. 
# Os números de suas cartelas entre 1 a 30, e você terá 10 participantes. Cada cartela terá 12 números (4,3)
'''
bingo = np.random.randint(1, 31, size=(10, 4, 3)) # Não esquecer de colocar +1 no 30, no caso 31
print(bingo)'''

# Faça o reshape de suas cartelas para que haja 5 cartelas de 4 linhas e 6 colunas

bingo = np.random.randint(1, 31, size=(10, 4, 3))
reshaped_array = bingo.reshape(5, 4, 6)
print(reshaped_array)









