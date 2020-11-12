import barajaC

palos = ["o", "c", "b", "e"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "s", "c", "r"]


mibaraja = barajaC.Baraja(palos, numeros)

print(mibaraja.mazo)
mibaraja.barajar()
print(mibaraja.mazo)
print(mibaraja.repartir(5,5))

