import baraja

class Baraja():
    
    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazo = baraja.crearBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazo)

    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range (num_jugadores):
            jugadores.append([])
        
        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                    jugadores[jugador].append(self.mazo.pop(0))

        return jugadores
