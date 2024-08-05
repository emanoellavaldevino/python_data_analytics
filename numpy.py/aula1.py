import numpy as np

# Fazendo uma lista simples 
''' 
l = [1, 2, 3, 4]  
arr1 = np.array(l)
print(arr1) ''' 

 # np.zeros 
 # Ele recebe sempre uma tubla, que são parênteses
 # Criado uma array da forma (3, 4) preenchidos com zeros. A tupla '(3, 4)' terá 3 linhas e 4 colunas.
''' 
array_zeros = np.zeros((3, 4)) 
print(array_zeros) '''  

# Criação de uma lista números inteiros usando range
# A função list() converte o objeto range em uma lista
# O range (0, 3) cria uma sequência de números de 0 a 2 (não inclui 3)
'''
array_zeros = list(range(0, 3))
print(array_zeros) '''

# A função np.arange cria um array com uma sequência de números. 
# Neste caso, cria uma sequência de número de 1 até 10(não inclui 11    )
'''
arr_range = np.arange(1, 11)
print(arr_range)'''

# Como saber o tipo?
'''print(type(arr_range))'''

# Random cria uma lista aleatórias de números em um intervalo de [0.0, 1.0]
# A forma do array é especificada pela tupla fornecida.
# Neste caso, foi pedido na tupla '(3, 3)' e foi gerado terá 3 linhas e 3 colunas.
# Random: Tipo float
''' arr = np.random.random((3, 3))
print(arr) '''

# Crie um array com 4 linhas e 3 colunas com valores aleatórios
# Tipo float
'''
arr1 = np.random.random((4, 3))
print(arr1) '''

# Crie um array com 5 colunas e 10 linhas inicializados com zeros
'''
arr2 = np.zeros((10, 5))
print(arr2) '''

# Crie uma array de números inteiros 3 linhas e 5 colunas com valores aleatórios
# Randint: Tipo inteiro
arra3 = np.random.randint(10, 30, size=(3,5))
print(arra3)