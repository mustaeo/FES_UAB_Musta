###
from pathlib import Path
from tempfile import TemporaryDirectory

# EXERCICIS - Fitxers TXT
# Treballa amb rutes rebudes per paràmetre i encoding="utf-8".
# Fes les proves dins de TemporaryDirectory per conservar les dades existents.
###
with TemporaryDirectory() as carpeta:
    # Exercici 1 - Bàsic - Desar un missatge
    # Implementa desar_missatge(ruta, missatge) i llegir_missatge(ruta).
    # Escriu tot el missatge amb mode w i recupera'l amb read().
    # Entrada de prova, "Sensor de tensió actiu\n".
    # llegir_missatge ha de retornar el mateix text amb el salt final.
    # Cas límit, el missatge "" es recupera com "".
    missatge_inicial = "Sensor de tensió actiu\n"

    def desar_missatge(ruta, missatge):
        with open(ruta, "w", encoding="UTF-8") as f:
            f.write(missatge)

    def llegir_missatge(ruta):
        with open(ruta, "r", encoding="UTF-8") as f:
            return f.read()

    ruta = Path("text.txt")
    desar_missatge(ruta, missatge_inicial)
    text = llegir_missatge(ruta)
    print(text)

    # Exercici 2 - Bàsic - Comptar lectures
    # Implementa comptar_lectures(ruta). Compta les línies que no queden buides
    # després d'aplicar strip(), sense convertir-les a nombres.
    # Contingut inicial, "20.0\n\n21.5\n   \n". Resultat esperat, 2.
    # Un fitxer buit ha de donar 0. Si falta, propaga FileNotFoundError.
    contingut_registre = "20.0\n\n21.5\n   \n"

    def comptar_lectures(ruta):
        with open(ruta, "r", encoding="UTF-8") as f:
            comptador = 0
            for linia in f:
                if linia.strip():
                    comptador+=1
        return comptador

    desar_missatge(ruta, contingut_registre)
    print(comptar_lectures(ruta))

    try:
        comptar_lectures(ruta)
    except FileNotFoundError:
        print("File not found")
                

    # Exercici 3 - Intermedi - Recuperar valors vàlids
    # Implementa llegir_valides(ruta). Converteix cada línia no buida amb float.
    # Si una línia genera ValueError, ignora-la i continua amb la següent.
    # El contracte d'aquest exercici només inclou decimals finits o text invàlid.
    # Entrada, "20.0\nerror\n\n22.0\n". Sortida, [20.0, 22.0].
    # Cas límit, totes les línies invàlides o buides han de retornar [].
    contingut_amb_error = "20.0\nerror\n\n22.0\n"

    def llegir_valides(ruta):
        lectures =[]
        with open(ruta, "r",encoding="UTF-8") as f:
            for linia in f:
                if linia.strip():
                    try:
                        lectures.append(float(linia.strip()))
                    except ValueError:
                        continue
        return lectures

    desar_missatge(ruta, contingut_amb_error)
    print(llegir_valides(ruta))


    # Exercici 4 - Repte opcional - Registre acumulatiu
    # Implementa afegir_esdeveniment(ruta, missatge) amb mode a.
    # Cada crida afegeix el missatge i un salt de línia.
    # Precondició, el missatge rebut no conté salts de línia.
    # Amb un fitxer inicialment absent i les crides amb "Inici" i "Aturada",
    # la lectura completa ha de donar "Inici\nAturada\n".
    # Repetir "Inici" ha d'afegir una tercera línia, conservant les dues anteriors.
    esdeveniments = ["Inici", "Aturada"]

    def afegir_esdeveniment(ruta, missatge):
        with open(ruta,"a",encoding="UTF-8") as f:
            f.write(missatge + "\n")
    afegir_esdeveniment(ruta, esdeveniments[0])
    afegir_esdeveniment(ruta, esdeveniments[1])
    afegir_esdeveniment(ruta, esdeveniments[0])
    print(llegir_missatge(ruta))

    # Exercici 5 - Intermedi - Filtrar temperatures
    # Implementa filtrar_temperatures(ruta_origen, ruta_desti, llindar).
    # Llegeix les temperatures de ruta_origen i desa a ruta_desti només les que
    # siguin iguals o superiors al llindar, una per línia i amb un decimal.
    # Entrada, "18.5\n25.7\n27.3\n20.5\n" i llindar 25.0.
    # La lectura del fitxer de destí ha de donar [25.7, 27.3].
    # Si cap temperatura supera el llindar, el fitxer de destí ha d'existir buit.
    temperatures_per_filtrar = "18.5\n25.7\n27.3\n20.5\n"
    llindar_temperatures = 25.0

    def filtrar_temperatures(ruta_origen, ruta_destino, llindar):
        temperatures = llegir_valides(ruta_origen)
        temperaturas_filtradas = []
        for temperatura in temperatures:
            if temperatura >= llindar:
                temperaturas_filtradas.append(temperatura)
        with open(ruta_destino, "w", encoding="UTF-8") as f:
            for temperatura in temperaturas_filtradas:
                f.write(f"{temperatura}:.1f\n")
        return temperaturas_filtradas


    desar_missatge(ruta, temperatures_per_filtrar)
    high_temp = Path(carpeta) / "temp_altas.txt"
    print(filtrar_temperatures(ruta,high_temp,llindar_temperatures))
    print(llegir_valides(high_temp))

    # Exercici 6 - Intermedi - Crear un resum d'un fitxer
    # Implementa crear_resum(ruta_origen, ruta_resum).
    # Llegeix temperatures i escriu un resum amb aquest format exacte:
    # "Nombre de lectures: 4\nMínima: 18.5 °C\nMàxima: 27.3 °C\nMitjana: 23.0 °C\n"
    # Entrada, "18.5\n25.7\n27.3\n20.5\n". Arrodoneix la mitjana a un decimal.
    # El fitxer buit ha de produir només:
    # "Nombre de lectures: 0\nNo hi ha dades per resumir.\n"
    def crear_resum(ruta_origen, ruta_resum):
        temperatures = llegir_valides(ruta_origen)
        with open(ruta_resum,"w", encoding="UTF-8") as f:
            f.write(f"nombre lectures: {len(temperatures)}\n")
            if not temperatures:
                f.write("no hay datos")
                return
            mitjana = sum(temperatures) / len(temperatures)
            f.write(f"minima: {min(temperatures):.1f}ºC\n")
            f.write(f"Max: {max(temperatures):.1f}ºC\n")
            f.write(f"mitjana: {mitjana:.1f}ºC\n")
    temperatures = Path(carpeta) / "temperatures.txt"
    desar_missatge(temperatures,temperatures_per_filtrar)
    resum = Path(carpeta) / "resum.txt"
    crear_resum (temperatures,resum)
    print(llegir_missatge(resum))