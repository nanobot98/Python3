import random

aleatorio = random.randrange(0, 3)
eligePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opción = int(input("Que eliges: "))

if opción == 1:
    eligeUsuario = "piedra"
elif opción == 2:
    eligeUsuario = "papel"
elif opción == 3:
    eligeUsuario = "tijera"
print("Tu eliges: ", eligeUsuario)

if aleatorio == 0:
    eligePc = "piedra"
elif aleatorio == 1:
    eligePc = "papel"
elif aleatorio == 2:
    eligePc = "tijera"
print("PC eligio: ", eligePc)
print("...")
if eligePc == "piedra" and eligeUsuario == "papel":
    print("Ganaste, El papel envuelve  la piedra")
elif eligePc == "papel" and eligeUsuario == "tijera":
    print("Ganaste, La tijera corta el papel")
elif eligePc == "tijera" and eligeUsuario == "piedra":
    print("Ganaste, La piedra pisa a la tijera")
if eligePc == "papel" and eligeUsuario == "piedra":
    print("Perdiste, El papel envuelve la piedra")
elif eligePc == "tijera" and eligeUsuario == "papel":
    print("Perdiste, La tijera corta el papel")
elif eligePc == "piedra" and eligeUsuario == "tijera":
    print("Perdiste, La piedra pisa la 1tijera")
elif eligePc == eligeUsuario:
    print("empate")