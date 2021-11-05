def sum(m):
    long = 0
    for number in m:
        long = long + number
    
    return long


n = int(input("Introduce el numero de elementos que va a tener la matriz: "))
m = []

for i in range(n):
    m.append(int(input("Numero para meter en la matriz: ")))

print(sum(m))