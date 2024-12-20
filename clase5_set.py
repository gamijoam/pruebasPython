contador = 0
lista_datos = []
for i in range(0,5):
    lista_datos.append(int(input(f'Ingresar numero: ')))
mi_set = set(lista_datos)
lista_datos.clear
for i in range(0,5):
    lista_datos.append(int(input(f'Ingresar numero: ')))
mi_set2 = set(lista_datos)

union_set = mi_set.union(mi_set2)
interseccion_set = mi_set.intersection(mi_set2)
diferencia_set = mi_set.difference(mi_set2)

print(f'La union es {union_set} - Interseccion es {interseccion_set} - Diferencia es {diferencia_set}')
