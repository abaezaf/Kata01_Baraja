import barajaC

palos = ["treboles", "corazones", "picas", "diamantes"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]


mibaraja = barajaC.Baraja(palos, numeros)

print(mibaraja.mazo)
mibaraja.barajar()
print(mibaraja.mazo)
