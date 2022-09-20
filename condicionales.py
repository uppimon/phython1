#Condicionales if  elif else 
#Nos permiten evaluar expresiones booleanas que de cumplirse realizan
#Una acción y en caso de que entonces realizan otra

#Evaluar si una persona es mas mayor de edad
#Nos diga es niño joven, adulto, bebé, muy mayor

genre = input("Ingresa tu género (H/M): ")
age = int(input('Ingresa tu edad: '))

mujer = "" 

if genre == "M":
    mujer = "a"



if age < 2:
    print(f"Eres un(mujer) bebé!")


elif age < 12:
    print(f"Eres un(mujer) niño")
elif age < 18:
    print(f"Eres un(mujer) joven")
elif age < 50:
    print(f"Eres un(mujer) adulto")
else:
    print(f"Eres muy(mujer) mayor!")