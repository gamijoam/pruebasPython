# Ingreso de cantidad de frutas
contador_fruta = int(input('Ingrese la cantidad de frutas deseadas: '))
lista_frutas = []

#Bucle para agregar frutas a una lista vacia
for i in range(0,contador_fruta):
    frutas = input('Ingrese nombre de la fruta: ')
    lista_frutas.append(frutas)

# Convertir lista en tupla e imprimir
lista_convertida = tuple(lista_frutas)
print(lista_convertida[0],lista_convertida[len(lista_convertida)-1])

#Creacion de diccionario
diccionario_persona = {'nombre':'Gabriel','edad':'25','ciudad':'Soledad'}

# Modificacion de diccionario por el usuario
modificacion_diccionario = input('Que dato desea modificar: Nombre - Edad - Ciudad ')
if modificacion_diccionario.lower() == 'nombre':
    modificacion = input('Cual es el dato nuevo: ')
    diccionario_persona['nombre'] = modificacion
    print(diccionario_persona)
elif modificacion_diccionario.lower() == 'edad':
    modificacion = input('Cual es el dato nuevo: ')
    diccionario_persona['edad'] = modificacion
    print(diccionario_persona)
else:
    modificacion = input('Cual es el dato nuevo: ')
    diccionario_persona['ciudad'] = modificacion 
    print(diccionario_persona)
