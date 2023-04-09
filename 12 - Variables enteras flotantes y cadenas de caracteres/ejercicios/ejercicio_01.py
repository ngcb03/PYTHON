""" 
Programa:Ver nombres ordenados de forma alfabética
Programador: Nicolas Camargo
Última actualización: 14-01-23

"""

# Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados
# en forma alfabética.

print("Persona #1")
nomPersona1 = input("Ingrese nombre: ")
print("Persona #2")
nomPersona2 = input("Ingrese nombre: ")

if nomPersona1<nomPersona2:
    print(nomPersona1)
    print(nomPersona2)
else:
    print(nomPersona2)
    print(nomPersona1)