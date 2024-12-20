# Creacion del archivo
with open('numeros.txt','w') as archivo:
    for i in range(1,11):
        archivo.write(f'{i}\n')
resultado = 0
with open('numeros.txt','r') as suma_numeros:
    for i in suma_numeros:
        resultado += int(i)

print(resultado)
