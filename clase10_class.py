class Coche():
    def __init__(self,marca,modelo,anio,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f'Marca: {self.marca} Modelo:{self.modelo} Año:{self.anio} Velocidad Maxima: {self.velocidad_maxima}  km/h')

mi_coche = Coche('Chevrolet','Optra',2014,150)
mi_coche.mostrar_info()
        
