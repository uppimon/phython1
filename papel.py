import random
while True:
    aleatorio = random.randrange(0, 3)
    eligePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input("Elige tu opción "))
    if opcion == 1:
        eligeUsuario = "Piedra"
    elif opcion == 2:
        eligeUsuario = "Papel"
    elif opcion == 3:
        eligeUsuario = "Tijera"
    print("Elegiste: ", eligeUsuario)
    if aleatorio == 0:
        eligePc = "Piedra"
    elif aleatorio == 1:
        eligePc =
