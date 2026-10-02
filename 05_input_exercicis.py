###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic = input("digues el nom del tecnic: ")
xarxa = input("Digues el nom de la xarxa que esta instalant")
print(f"el tecnic {tecnic} esta instalant la xarxa {xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Longitud en kilometres: "))
velocitat = float(input("Velocitat en Gbps: "))
temps = 8/velocitat
print(f"a l'enllaç de {longitud:.2f}Km, es tardará {temps} segons en enviar 1GB")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores = int(input("Introdueix hores de feina: "))
preu = float(input("Introdueix preu per hora: "))
preu_m= float(input("Introdueix tambe el preu del material: "))

print(f"El cost total es de {hores*preu + preu_m:.2f}€ ")