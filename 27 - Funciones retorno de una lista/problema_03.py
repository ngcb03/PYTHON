"""
Programador: Nicolas G. Camargo B.

Programa: Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.


Última modificación: 13-04-23

"""
# funciones
def cargaInfoPersonas():
  nombres = []
  edad = [] 
  cont = 0
  print("¡Registro información personal!")
  while cont < 5:
    print("Persona #1")
    nombres.append(input("Ingrese nombre completo: "))
    edad.append(int(input("Ingrese edad: ")))
    cont+=1
  return [nombres,edad]

def mayEdad(edades):
  mayores = []
  for f in edades:
    if f>=18:
      mayores.append(edades.index(f))
  return mayores

def promEdad(edades):
  sum = 0
  for f in edades:
    sum+=f
  prom = (sum//len(edades))
  return prom

def listarInfo(info):
  print("\nPersonas regitradas:")
  for f in range(0,len(info[0][0])):
    print("nombre:",info[0][0][f])
    print("edad:",info[0][1][f])
  print("\nMayores edad:")
  for f in range(0,len(info[1])):
    print("nombre:",info[0][0][info[1][f]])
    print("edad:",info[0][1][info[1][f]])
  print("\nPromedio edades:",info[2])


# bloque principal
infoPersonas = []
infoPersonas.append(cargaInfoPersonas())
infoPersonas.append(mayEdad(infoPersonas[0][1]))
infoPersonas.append(promEdad(infoPersonas[0][1]))
listarInfo(infoPersonas)