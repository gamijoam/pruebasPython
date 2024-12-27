class Motor:
    def __init__(self,tipo):
        self.tipo = tipo

    def encender(self):
        print('Motor Encendido')

class Coche:
    def __init__(self,marca,modelo,motor):
        self._marca = marca
        self._modelo = modelo
        self.motor = motor

    #Getter
    def get_marca(self):
        return self._marca
    def get_modelo(self):
        return self._modelo

    #Setter
    def set_nombre(self,marca):
        self._marca = marca
    def set_modelo(self,modelo):
        self._modelo = modelo

    def arrancar():
        print('Ya arrancando')
        self.motor.encender()


