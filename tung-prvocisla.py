import math
nPuvodni =12687862

n = nPuvodni
nD = math.sqrt(n)
nDown = math.floor(nD)
garbage = [2]

listPossible = []
for i in range(3, nDown,2):
    listPossible.append(i)

#del listPossible[0::2]
# slice sequence[start:stop:step] = even numbers
print("listPossible")
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


delitele = delitele1
delitele.append(delitele2[-1])
print(delitele)

nKontrola = 1

for i in delitele:
    nKontrola = nKontrola * i

print(nKontrola)
print (nPuvodni)



