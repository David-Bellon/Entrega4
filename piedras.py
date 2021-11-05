from math import pi
from random import randint as rd

ganador = False
piedras_Tablero = rd(2, 10)

j1 = True
j2 = False

while(ganador == False):
    if j1:
        print("Turno del Jugador 1")
    else:
        print("Turno del Jugador 2")
    print("Piedras en el tablero:", piedras_Tablero)

    if(piedras_Tablero >= 2):
        if piedras_Tablero == 2 or piedras_Tablero == 3 or piedras_Tablero == 5:
            piedras_Tablero = 0
            if j1:
                print("El jugador 1 quita 2, 3 o 5 piedras")
            else:
                print("El jugador 2 quita 2, 3 o 5 piedras")
            print("Piedras restantes:", piedras_Tablero)

        else:
            if piedras_Tablero - 2 == 1 or piedras_Tablero - 3 == 1 or piedras_Tablero - 5 == 1:
                piedras_Tablero = 1
                if j1:
                    print("El jugador 1 quita 2, 3 o 5 piedras")
                else:
                    print("El jugador 2 quita 2, 3 o 5 piedras")
                print("Piedras restantes:", piedras_Tablero)

            else:
                if piedras_Tablero == 7:
                    piedras_Tablero = piedras_Tablero - 3
                    if j1:
                        print("El jugador 1 quita 3 piedras")
                    else:
                        print("El jugador 2 quita 3 piedras")
                    print("Piedras restantes:", piedras_Tablero)

                if piedras_Tablero == 8:
                    piedras_Tablero = piedras_Tablero - 5
                    if j1:
                        print("El jugador 1 quita 5 piedras")
                    else:
                        print("El jugador 2 quita 5 piedras")
                    print("Piedras restantes:", piedras_Tablero)
                if piedras_Tablero == 9:
                    piedras_Tablero = piedras_Tablero - 5
                    if j1:
                        print("El jugador 1 quita 5 piedras")
                    else:
                        print("El jugador 2 quita 5 piedras")
                    print("Piedras restantes:", piedras_Tablero)
                if piedras_Tablero == 10:
                    piedras_Tablero = piedras_Tablero - 2
                    if j1:
                        print("El jugador 1 quita 2 piedras")
                    else:
                        print("El jugador 2 quita 2 piedras")
                    print("Piedras restantes:", piedras_Tablero)
                    
    else:
        ganador = True
    j1 = not j1
    j2 = not j2

if j1 == True:
    print("Ganador juegador 1")
else:
    print("Ganador jugador 2")