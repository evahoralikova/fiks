import math
nPuvodni =4352

n = nPuvodni
nD = n/2
nDown = math.floor(nD)
garbage = []
print("odmocnina:")
print (nDown)

listPossible = [2,3,5,7]
for i in range(2, nDown):
    listPossible.append(i)

del listPossible[0::2]
# slice sequence[start:stop:step] = even numbers
print("nezbavene 2: ")
print(listPossible)

for i in listPossible:
    if i% 3 == 0 :
        garbage.append(i)
    elif i% 5 == 0:
        garbage.append(i)
    elif i% 7 == 0:
        garbage.append(i)

prvocislaSet = {*listPossible}
nePrvocislaSet = {*garbage}
prvocislaSet.difference_update(nePrvocislaSet)

prvocisla = [*prvocislaSet, 2,3,5,7]
prvocisla.sort()
nePrvocisla = [*nePrvocislaSet]
nePrvocisla.sort()

print("neprovcisla:")
print(nePrvocisla)
(print("prvocisla:"))
print(prvocisla)


delitele1 = []
delitele2 = []
for i in prvocisla:
    while (n % i == 0 ):  # je delitelne
        vysledek = n / i
        n = n / i
        delitele2.append(vysledek)
        delitele1.append(i)


print("delitele1")

print(delitele1)

print("delitele2")

print(delitele2)

nKontrola = 1

for i in delitele1:
    nKontrola = nKontrola * i
print(nKontrola)
print (nPuvodni)


