# Este ejercicio consiste en crear una implementación del juego pares o nones, en el que jugaremos contra la máquina. Para esta implementación usaréis la librería <<random>> de la cual ya hemos hablado.

# La implementación es libre, pero tiene que ser un jugador contra la máquina. Podéis hacerlo al mejor de tres, al que gane 4, como vosotr@s queráis.

# Nos gustaría que uséis funciones para que os acostumbréis a la creación de las mismas.

# Ejercicio pares o nones

import random
from colorama import Fore
import os


def pares_nones():
    print(Fore.GREEN,"************* Bienvenido al juego de pares o nones | The bridge *************")
    print("Elige pares o nones")
    eleccion = input()
    
    if eleccion == "pares":
        print("Has elegido pares")
    if eleccion == "nones":
        print("Has elegido nones")
    print("Ahora elige un número del 1 al 5")
    numero = int(input())
    if numero > 5:
        print("El número no es válido")
    else:
        print("Has elegido el número", numero)
    numero_maquina = random.randint(1, 5)
    print("La máquina ha elegido el número", numero_maquina)
    suma = numero + numero_maquina
    print("La suma de los números es", suma)
    if suma % 2 == 0:
        print("La suma es par")
        if eleccion == "pares":
            print("¡Has ganado!")
        else:
            print("¡Has perdido!")
    else:
        print("La suma es impar")
        if eleccion == "nones":
            print("¡Has ganado!")
        else:
            print("¡Has perdido!")
    print("¿Quieres jugar otra vez? (si/no)")
    respuesta = input()
    if respuesta == "si":
        os.system("cls")
        pares_nones()
    else:
        print("Gracias por jugar")
        exit()

pares_nones()