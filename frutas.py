s = int(input("Punto de partida casa: "))
t = int(input("Punto final de la cas: "))

a = int(input("Posicion del manzano: "))
b = int(input("Posicion del naranjo: "))

m = int(input("Numero de manzanas que caen: "))
n = int(input("Numero de naranjas que caen: "))


def cont(m, n):
    naranjas_rango = 0
    manzanas_rango = 0
    for naranjas in n:
        if naranjas >= s_0 and naranjas <= t_0:
            naranjas_rango += 1
    
    for manzanas in m:
        if manzanas >= s_0 and manzanas <= t_0:
            manzanas_rango += 1

    return [manzanas_rango, naranjas_rango]



#Pasar a un mismo sistema de referencia
a_0 = 0
s_0 = s - a
t_0 = t - a
b_0 = b - a


manzanas = []
naranjas = []

for i in range(m):
    manzanas.append(int(input("Distancia de la manzana al arbol: ")))

for i in range(n):
    naranjas.append(int(input("Distancia de la naranja al arbol:")) + b_0)



print(cont(manzanas, naranjas))