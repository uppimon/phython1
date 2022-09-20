#Lee la edad de alguien
#Resta a esta edad y se llama last_years
#first_years será igual a los 2 por 10.5
#Multiplicar  los años restantes (last_years) por 4
#Sumar los first_years con el resultado anterior
#Imprimir lo siguiente "Tines 24 años que equivalen a 78 años perrunos"


def calcular_age_dog(age_human):
    if age_human <= 2:
        return age_human * 10.5
    else:
        return 21 + (age_human - 2) * 4

        #if edad_persona > 0:
        #    resultado = calcular_edad_perro(edad persona)
        #    print(f"La edad del perro en años seria {result}")

age_human = int(input('Digite la edad en años de la persona: '))
age_dog = calcular_age_dog(age_human)

print(f"Tines {age_human} años que equivalen a {age_dog} años perrunos")
