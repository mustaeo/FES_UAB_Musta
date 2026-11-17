###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}")

saludar_a("Musta","Como estas")
saludar_a("Musta")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(numero):
    return numero%2 == 0
print(es_parell(1))
print(es_parell(4))

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma = 0
    for num in numeros:
        suma += num
    mitjana = suma/len(numeros)
    return mitjana

nums = [1, 5, 10, 15, 20]
print(mitjana(nums))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    suma=0
    for num in args:
        suma+=num
    return suma

print(sumar_tot(1, 3))
print(sumar_tot(1, 3, 5, 10, 15))
print(sumar_tot(1, 3, 5, 10, 20, 15, 7, 8, 9, 1))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit = 10):
    for x in range(1, limit+1):
        mult = numero * x
        print(f"{numero}*{x} = {mult}"  )
taula_multiplicar(2)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les
#  dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom = "Musta", edat = 21, grau = "Enginyeria en telecomunicacions")


# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.

def factorial(numero):
    factor = 1
    suma = 1
    while factor <= numero:
        suma*=factor
        factor+=1
    return suma
print(f"el factorial de 5 es {factorial(5)}")

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.

def comptar_vocals(text):
    text = text.lower()
    vocals = "aeiouàèéíòóúïü"
    comptador = 0
    for lletra in text:
        if lletra in vocals:
            comptador+=1
    return comptador
print(comptar_vocals("Hola que tal"))

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.

def minim_i_maxim(numeros):
    minim = numeros[0]
    maxim = numeros[0]
    for num in numeros:
        if num > maxim:
            maxim = num
        elif num < minim:
            minim = num
    return minim, maxim
minim, maxim = minim_i_maxim([1,3,5,7,10,-5,30,20])
print(f"el valor minimo es {minim} y el valor maxim es {maxim}")


# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.

def es_palindrom(text):
    text_l = text.lower()
    return text_l == text_l[::-1]

print(es_palindrom("anna"))
print(es_palindrom("Hola"))