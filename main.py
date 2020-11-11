import baraja

ordenada = baraja.crearBaraja()
print("Primera baraja, que está bien ordenadita", ordenada)

desordenada = baraja.crearBaraja()
baraja.barajar(desordenada)
print("Baraja desordenada porque seh", desordenada)