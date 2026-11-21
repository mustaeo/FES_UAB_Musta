###
# EXERCICIS (excepcions)
# Tots els textos d'entrada es proporcionen per evitar entrada interactiva.
###
import math
from pathlib import Path
from tempfile import TemporaryDirectory
# Exercici 1 - Bàsic. Conversió segura de tensions
# Per a cada text de tensions, intenta convertir-lo amb float.
# Captura ValueError i mostra 'Tensió incorrecta' en aquest cas.
# Utilitza else per mostrar la conversió quan sigui correcta.
# Sortida esperada, una línia per entrada: 3.3 / Tensió incorrecta / 0.0.
# Cas límit: '0' és una mesura vàlida.
tensions = ["3.3", "avaria", "0"]
# TODO: escriu el bucle i el tractament de ValueError.

for text in tensions:
    try:
        temperatura = float(text)
    except ValueError:
        print("Tensio incorrecta")
    else:
        print(temperatura)

# Exercici 2 - Bàsic. Humitat amb contracte
# Defineix validar_humitat(text) que retorni un float finit dins [0, 100].
# Genera ValueError per a text no numèric, valors no finits o fora de rang.
# Utilitza math.isfinite després de convertir el text.
# Entrades: '0', '100', '45.5', '-1', '101', 'nan', 'inf', 'error'.
# Retorns esperats per a les tres primeres: 0.0, 100.0 i 45.5.
# La resta han de produir ValueError, gestionat en les demostracions.
entrades_humitat = ["0", "100", "45.5", "-1", "101", "nan", "inf", "error"]
# TODO: defineix la funció i mostra resultats o un missatge de rebuig.

def validar_humitat(text):

    humitat = float(text)
    if (humitat>100 or humitat<0):
        raise ValueError("La humitat ha d'estar dins del rang")
    if not math.isfinite(humitat):
        raise ValueError("Ha de ser un numero finit")
    return humitat
print(validar_humitat(45.5))


# Exercici 3 - Intermedi. Fitxer absent i finalització
# Dins de TemporaryDirectory crea només una ruta a 'absent.txt' amb Path.
# Intenta obrir-la en mode lectura, amb encoding='utf-8'.
# Captura FileNotFoundError i mostra 'Fitxer absent'.
# Utilitza finally per mostrar 'Intent acabat' tant si hi ha error com si no.
# Sortida esperada: Fitxer absent / Intent acabat.
# Segona prova: crea un fitxer temporal que contingui 'T1=21.5' i repeteix.
# Sortida esperada: T1=21.5 / Intent acabat.
# Mantén tots els fitxers dins de la carpeta temporal.
# TODO: importa Path i TemporaryDirectory i prova els dos camins.

with TemporaryDirectory() as carpeta:
    ruta = Path(carpeta) / "absent.txt"
    try:
        with open(ruta, encoding="UTF-8") as f:
            contingut = f.read()
    except FileNotFoundError:
        print("Fitxer Absent")
    else:
        print(contingut)
    finally:
        print("Intent acabat")

    ruta = Path("text.txt")
    try:
        with open(ruta, encoding="UTF-8") as f:
            contingut = f.read()
    except FileNotFoundError:
        print("Fitxer Absent")
    else:
        print(contingut)
    finally:
        print("Intent acabat")


# Exercici 4 - Repte opcional. Filtrar lectures de temperatura
# Defineix filtrar_temperatures(textos) que retorni (valides, rebutjades).
# valides és la llista de floats finits dins del rang simulat [-40, 85] °C.
# rebutjades és el nombre d'entrades que no es poden acceptar.
# Crea una funció validar_temperatura(text) i reutilitza-la al bucle.
# Entrada següent. Retorn esperat: ([-40.0, 21.5, 85.0], 3).
# Amb [] ha de retornar ([], 0). Amb ['nan', 'inf'] ha de retornar ([], 2).
textos = ["-40", "21.5", "85", "86", "avaria", "nan"]
# TODO: captura ValueError per cada lectura i continua amb les següents.

def filtrar_temperatures(textos):
    rebutjades = 0
    valides = []
    for text in textos:
        try:
            text = validar_temperatura(text)
        except ValueError:
            rebutjades+=1
        else:
            valides.append(text)
       
    return valides, rebutjades

def validar_temperatura(text):
    temperatura = float(text)
    if(temperatura>85 or temperatura < -40):
        raise ValueError("Temperatura fora del rang")
    if not math.isfinite(temperatura):
        raise ValueError("La temperatura no es finita")
    return temperatura

print(filtrar_temperatures(textos))
