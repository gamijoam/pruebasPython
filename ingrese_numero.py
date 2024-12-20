numero = int(input('Ingrese un numero: '))
resultado = 0
contador = 0
if numero > 10 :
    print('Numero grande')
else:
    print('El numero es pequeño')

for i in range(1,numero + 1):
    print(i)

while contador != numero:
    lista_numero = range(1,numero +1)
    resultado += lista_numero[contador]
    contador += 1
    print(resultado)
