# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

negativos=0
positivos=0
mult15=0
sumaPares=0

for x in range(10):
  num = int(input("Ingrese valor -> "))
  if num>0:
    positivos+=1
    if num%2==0:
      sumaPares+=num
    if num%15==0:
      mult15+=1
  else:
    negativos+=1

print("Cantidad negativos ->",negativos)
print("Cantidad positivos ->",positivos)
print("Cantidad de multiplos de 15 ->",mult15)
print("Suma pares ->",sumaPares)