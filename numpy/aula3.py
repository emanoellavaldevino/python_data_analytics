import numpy as np

# dtype como argumento
# O float32 é um tipo de dado de ponto flutuante de 32 bits,
# que usa menos memória do que o float64 (o padrão do NumPy para floats) mas com menor precisão.
'''
aula3 = np.array([2.14, 6.25, 160.87], dtype=np.float32)
print(aula3.dtype)
print(aula3) '''

# Conversão: Imprime o array convertido para inteiros
# Lembrando que False é 0, e True é 1
'''
aula3 = np.array([[True, False], [True, True]], dtype=np.bool_)
converter_array = aula3.astype(np.int32)
print("\n Array convertido para inteiros: ")
print(converter_array)'''

# Coeção
# Cria um array com diferentes tipos de dados
'''
aula3 = np.array(["pedra", False, 42, 42.42])
print(aula3.dtype) '''

# Exercício de aula 3
# Por padrão, ao criar um array NumPy com valores de ponto flutuante, o NumPy utiliza float64
'''
aula3 = np.array([5.4, 6.7, 2.1])
print(aula3.dtype) '''

# Exercício de aula 3
# Tipo Int
'''
aula3 = np.array([1, 6, 13])
print(aula3.dtype)'''

# Exercício de aula 3
# Tipo String
'''
aula3 = np.array(['Emanoella', 'Tudo', 'oi'])
print(aula3.dtype)'''

# Exercício de aula 3
# Qual é o tipo de dados em um numpy array?
'''
aula3 = np.array([2, 6, 2.4])
print(aula3.dtype)'''

# Exercício de aula 3
'''
aula3 = np.array([True, 3, False])
print(aula3.dtype)'''

# Exercício de converter
# Cria um array com inteiros e um número de ponto flutuante
aula3 = np.array([3, 6, 2.1])
converter_array = aula3.astype(np.int32)
print(converter_array)
print(aula3.dtype)

