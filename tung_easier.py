import math
from timeit import default_timer as timer

start = timer()
g = open("myfile.txt", "w")
with open("input (4).txt") as f:
   x=1
   for x in range(1, int(f.readline())+1):
       nebezpecnost = 1  # jednicka deli urcite
       n = int(f.readline())
       if n < 10 ** 12:
           nD = math.sqrt(n)
           nDown = math.floor(nD)
           if n%2 != 0:
               for i in range(3, nDown, 2):  # jednicka uz tam je
                   if n % i == 0:
                       vysledek = n / i
                       if vysledek == nDown:
                           nebezpecnost = nebezpecnost + 1
                       else:
                           nebezpecnost = nebezpecnost + 2
               g.write(str(nebezpecnost))
               g.write("\n")
               print(nebezpecnost)

           else:
               for i in range(2, nDown + 1):  # jednicka uz tam je
                   if n % i == 0:
                       vysledek = n / i
                       if vysledek == nDown:
                           nebezpecnost = nebezpecnost + 1
                       else:
                           nebezpecnost = nebezpecnost + 2
               g.write(str(nebezpecnost))
               g.write("\n")
               print(nebezpecnost)
       else:
           g.write("O velky Tung")
           g.write("\n")
           print("O velky Tung")

f.close()
end = timer()
print(end - start)

