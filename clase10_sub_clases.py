class Animal():
    def hacer_sonido(self):
        print('El animal hace cualquier sonido')

class Gato(Animal):
    def hacer_sonido(self):
        print('El gato maulla')


felino = Gato()
felino.hacer_sonido()
