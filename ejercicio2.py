def compare(ls1, ls2):
    lucia = 0
    carlos = 0
    for i in range(len(ls1)):
        if ls1[i] != ls2[i]:
            if ls1[i] > ls2[i]:
                lucia += 1
            else:
                carlos += 1
    return [lucia, carlos]

a = []
b = []
#Indicamos cuantos datos vamos a manejar, en este caso son 3 pero podrian ser mas
datos = int(input("Cuantos datos vamos a manejar: "))

#Añadimos todos los datos por orden a cada uno de los arrays para comparar.
for i in range(datos):
    a.append(int(input("Dato para lucia: ")))
    b.append(int(input("Dato para carlos: ")))

print(compare(a, b))