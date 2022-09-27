#Script que juega piedra papel y tijera con el Usuario
import random
#Leer elección del Usuario
user =input("Elige: Piedra, Papel o Tijera: ")

#Generar elección de la Maquina
aleatorio = random.randint(1,3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine = "papel"
else:
    aleatorio = "tijera"
#Comparar para determinar quien gana
print("El usuario eligió", user,   "la maquina eligió ", machine)
if machine== 'piedra' and user=='papel':
    print("Gana el usuario ")
elif machine=='papel' and user== 'piedra':
    print("Gana la maquina ")
elif machine=='tijera' and user== 'papel':
    print("Gana la maquina")
elif machine== 'piedra' and user== 'piedra':
    print("Es un empate")
elif machine=='tijera' and user== 'piedra':
    print("Gana el usuario")
elif machine== 'piedra' and user== 'tijera':
    print("Gana la maquina")
elif machine=='papel' and user== 'tijera':
    print("Gana el usuario")
elif machine== 'piedra' and user=='tijera':
    print("Gana la maquina ")
elif machine== 'papel' and user=='papel':
    print("Juega de nuevo ")



