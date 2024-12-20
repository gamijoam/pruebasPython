# Tupla de numeros primos
num_primos = (2,3,5,7,11)
diccionario_numeros = {}
for i in range(1,len(num_primos)+1):
    diccionario_numeros[num_primos[i-1]] = i
print(num_primos)
print(diccionario_numeros)
