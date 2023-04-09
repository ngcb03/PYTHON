# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el
# número es positivo, negativo o nulo (es decir cero)

num = int(input("Ingresa un valor entero: "))
print("¡El valor ingresado es")
if num>=0:
  if num==0:
    print("nulo!")
  else:
    print("positivo!")  
else:
  print("negativo!")    