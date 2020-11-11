import baraja

class Baraja():
    
    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazo = baraja.crearBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazo)

