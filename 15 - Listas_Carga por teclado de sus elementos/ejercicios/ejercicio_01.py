"""
Programador: Nicolas G. Camargo B.

Programa: Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

Última modificación: 29-01-23

"""

sueldos = []
sumG = 0 # Suma los sueldos para luego obtener el promedio

for f in range(5):
  sueldos.append(float(input("Ingresar sueldo operario: ")))
  sumG += sueldos[f]

print("Sueldos operarios: ",sueldos)
print("Promedio sueldos:",(sumG/5))