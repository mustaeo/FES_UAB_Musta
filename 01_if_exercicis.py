###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
lvl = float(input("Introdueix el nivell de senyal Wi-Fi (en dBm): "))
if lvl >= -50:
    print("excelent")
elif -67 < lvl <= -50:
    print("bona")
elif -75 <= lvl < -67:
    print("feble")
else:
    print("molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia = float(input("Introdueix la potencia optica en dBm: "))
if -27 <= potencia <= -8:
    print("Acceptable")
elif potencia > -8:
    print("Massa alt")
else:
    print("massa baix")
# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix el consum de GB: "))
if consum > 20:
    print(f"S'ha excedit el consum de GB per {consum - 20}GB")
else:
    print("Esta dins del limit")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los = int(input("Indicador LOS esta ences? (1 o 0): "))
internet =int(input("indicador Internet esta ences? (1 o 0): "))
los_t = los == 1
internet_t = internet == 1
if los_t and internet_t:
    print("La connexio sembla funcionar correctament")
elif los_t and not internet_t:
    print("Cal comprovar el servei del proveidor")
elif not los_t and internet_t:
    print("Cal revisar el cable de fibra")
else:
    print("Cal revisar el cable de fibra i comprovar el servei del proveidor")


# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bat = float(input("Introdueix el percentatge de bateria del SAI: "))
if 0 > bat > 100:
    print("Valor fora del rang")
elif bat < 20:
    print("Nivell crític")
elif 20 <= bat < 50:
    print("Nivell baix")
else:
    print("Nivell suficient")