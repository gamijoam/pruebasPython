try:
    numero_1 = int(input('Ingresar un numero: '))
    numero_2 = int(input('Ingresar un numero: '))
    print(numero_1 % numero_2)

# ValueError
#ZeroDivisionError
except Exception as e:
    if type(e).__name__ == 'ValueError':
        print('Esta introduciendo un valor no numerico')
    elif type(e).__name__ == 'ZeroDivisionError':
        print('No se puede dividir con 0')
finally:
    print('El programa a finalizado')
