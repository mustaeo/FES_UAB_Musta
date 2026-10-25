###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
comptador = 10
while comptador > 0:
    print(comptador)
    comptador -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
comptador = 0
suma = 0
while comptador <= 20:
    if(comptador % 2 == 0):
        print(comptador)
        suma +=comptador
    comptador +=1

print(suma)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Introdueix un numero enter positiu: "))
factor = 1
suma = 1
while factor <= numero:
    suma*=factor
    factor+=1
print(f"El factorial de {numero} es {suma}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
passw = ""
while(len(passw) < 8):
    passw = input("Introdueix una contrasena de almenys 8 caracters: ")
    if(len(passw)<8):
        print("la contraena ha de ser de almenys 8 caracters. Torna-ho a provar")
print("contrasena valida")


# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num = int(input("Introdueix un numero enter: "))
comptador = 1
res = 0
while comptador <= 10:
    res = num*comptador;
    print(f"{num}*{comptador} = {res}")
    comptador+=1
# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
num = int(input("Introdueix un numero enter positiu: "))
comptador = 2
while comptador <= num:
    divisor = 2
    primo = True
    while divisor*divisor <= comptador:
        if(comptador % divisor == 0): #compruebo si comptador entre el divisor da entero
            primo = False
            break
        divisor += 1
    if(primo == True):
        print(comptador)
    comptador+=1
# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
num = -1
suma = 0
while num != 0:
    num = int(input("Introdueix numeros enters: "))
    if num == 0:
        continue
    suma += num
print(f"Has introduit 0, la suma de tot es {suma}")
# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
num = int(input("Introdueix un numero enter positiu: "))
comptador = 0
while num > 0:
    num //= 10
    comptador+=1
print(f"Tiene {comptador} digitos")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
num = int(input("indica quants termes de la sequencia fibonacci vols veure: "))
anterior = 0
actual = 1
comptador = 0
while comptador < num:
    print(anterior)
    seguent = anterior + actual
    anterior = actual
    actual = seguent
    comptador += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
secret = 7
num = 0
while num != secret:
    num = int(input("Intenta endenvinar el numero secret:"))
    if( num<secret): print("Incorrecte, el numero introduit es menor al secret")
    elif( num>secret): print("Incorrecte, el numero introduit es major al secret")
print("Has endevinat el numero!!")