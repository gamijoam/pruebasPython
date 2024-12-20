lista = [x for x in range(1,40,2)]

def numero_cuadrado():
    for i in range(10):
        yield i**2

gen = numero_cuadrado()

for numero in gen:
    print(numero)
print(lista)
