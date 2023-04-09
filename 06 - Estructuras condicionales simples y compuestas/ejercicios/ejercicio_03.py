# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un 
# número entero)

num = int(input("Ingresa un valor positivo menor a 100: "))
if num<100:
  if num<9:
    print("¡El valor tiene 1 dígito!")
  else:
    print("¡El valor tiene 2 dígitos!")  
else:
  print("¡El valor no cumple las condiciones solicitadas!")    