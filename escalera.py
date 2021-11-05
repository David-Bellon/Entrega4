def escalera(n):
    for i in range(len(n)):
        for j in range(len(n) - i - 1, -1):
            print(" ", end="")
        print(n[:(i + 1)], end="")
        print("\n", end="")

p = int(input("Numero de peldaños de la escalera: "))
ls = []

for i in range(p):
    ls.append("#")

s = ""
for i in range(p):
    s = ls[i] + s

print(escalera(s))