# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.

mitupla = ("BCN", "MADRID", "VALENCIA", "MALAGA", "SEVILLA")
print(mitupla[1])
print(mitupla[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.

tupla2 = (1,2,3,4,5,6,7,3,2,1,3,3)
recuento = tupla2.count(3)
print(recuento)

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.

def tuplefunct(nums):
    return sorted(nums)
print(tuplefunct(tupla2))