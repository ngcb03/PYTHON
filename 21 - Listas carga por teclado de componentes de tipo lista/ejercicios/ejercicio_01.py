"""
Programador: Nicolas G. Camargo B.


Programa: Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.


Última modificación: 02-03-23

"""
# Definimos listas
paises=[]
temperaturas=[[],[],[]]
cont=0

# Solicitamos paises y temperaturas x meses
while cont<3:
  paises.append(input("Ingrese país: "))
  temperaturas[cont].append(float(input("Ingrese temperatura media mes 1: ")))
  temperaturas[cont].append(float(input("Ingrese temperatura media mes 2: ")))
  temperaturas[cont].append(float(input("Ingrese temperatura media mes 3: ")))
  cont+=1
  print()

# Listamos paises / temperatura x mes / temperatura trimestral
tempTrimestral=[]
print()
for k in range(len(paises)):
  print("Pais:",paises[k])
  print("Temperatura media meses:")
  print("mes 1:",temperaturas[k][0])
  print("mes 2:",temperaturas[k][1])
  print("mes 3:",temperaturas[k][2])
  tempTrimestral.append((temperaturas[k][0]+temperaturas[k][1]+temperaturas[k][2])/3)
  print("Temperatura media trimestral:",tempTrimestral[k])
  print()

print()

# País con mayor temperatura trimestral
mayorTemp=tempTrimestral[0]
poscPais=0 # indica o lugar del país
for x in range(len(tempTrimestral)-1):
  if tempTrimestral[x]<tempTrimestral[x+1]:
    mayorTemp=tempTrimestral[x+1]
    poscPais=x+1

# Listamos país con mayor temperatura trimestral
print("País con mayor temperatura:",paises[poscPais],"->",mayorTemp)