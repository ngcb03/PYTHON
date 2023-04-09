"""
Programador: Nicolas G. Camargo B.

Programa: Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
  Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y 
  cuántas más bajas.

Última modificación: 29-01-23

"""
alturas = [] # Lista vacía para registrar alturas
cont = 0 # Contador bucle
sumaAlt = 0 # Suma alturas para obtener promedio
menProm = 0 # alturas menores al promedio
mayProm = 0 # alturas mayores al promedio

while cont<5:
  print("Personas #",cont+1)
  alturas.append(float(input("Ingrese altura: ")))
  sumaAlt+=alturas[cont]
  cont+=1

print()
promAlt = sumaAlt/5
print("Promedio altura:",promAlt)
print()

for f in alturas:
  if f>promAlt:
    mayProm+=1
  else:
    menProm+=1

print("Personas alturas superiores al promedio:",mayProm)
print("Personas alturas inferiores al promedio:",menProm)