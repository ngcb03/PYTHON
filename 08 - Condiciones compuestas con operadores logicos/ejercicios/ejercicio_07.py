# Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se 
# calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

mayor=0
menor=0

num1 = int(input("Ingresa primer valor: "))
num2 = int(input("Ingresa segundo valor: "))
num3 = int(input("Ingresa tercer valor: "))

if num1>num2 and num1>num3:
  mayor=num1
  if num2>num3:
    menor=num3
  else:
    menor=num2
else:
  if num2>num3:
    mayor=num2
    if num3>num1:
      menor=num1
    else:
      menor=num3
  else:
    mayor=num3
    if num2>num1:
      menor=num1
    else:
      menor=num2  

diferencia=mayor-menor
print("Valor mayor:",mayor)
print("Valor menor:",menor)
print("Diferencia entre",mayor,"y",menor,"->",diferencia)          