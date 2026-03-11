from decimal import Decimal, ROUND_HALF_UP
print("Hello", "world", sep = "//")
a = 'nice'
print("Python is {}".format(a))
n = 14.364958644869048
print(f"{n:.2f}")
print("{:.2f}".format(n))
print("%.2f" % n)
print(format(n, ".2f"))
print(str(round(n, 2)))
print(Decimal(n).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP))
a = "2"
b = 5
print(int(a) + b)
print(id(b)) # adresa variabilei b
c = ["Timisoara", "Resita", "Arad", "Oradea"]
print(c)
print(id(c))
c.append("Cluj")
print(c)
print(id(c))
c += ["Sibiu"]
print(c)
print(id(c))
c.insert(6, "Brasov")
print(c)
print(id(c))
binC = bin(3)
print(binC)
x = 2.0
y = 5
z = "abc"
print(type(x))
print(type(y))
print(type(z))
print(5/2)
print(5//2)
print(z*3)
q = input("Introduceti un numar: ")
print(type(q))

