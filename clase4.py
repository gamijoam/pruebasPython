
try:
# Funcion para multiplicar dos numeros
    def multiplicar(a,b):
        return a*b

    # Variables a multiplicar
    numero1 = int(input('Ingrese primer numero a multiplicar: '))
    numero2 = int(input('Ingrese segundo numero a multiplicar: '))
    print(multiplicar(numero1,numero2))


# Captura de error
except ValueError:
    print('No ingreso un numero')
