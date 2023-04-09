# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles # (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

equilatero=0
isosceles=0
escaleno=0

n = int(input("Cantidad de datos a registrar: "))

for x in range(n):
  print("Triangulo #",x+1)
  lado1 = int(input("Medida lado #1 ->"))
  lado2 = int(input("Medida lado #1 ->"))
  lado3 = int(input("Medida lado #1 ->"))
  
  if lado1==lado2 and lado1==lado2 and lado2==lado3:
    print("¡Equilatero!")
    equilatero+=1
    print
  else: 
    if lado1==lado2 or lado1==lado3 or lado2==lado3:
      print("¡Isósceles!")
      isosceles+=1
      print
    else:
      print("¡Escaleno!")
      escaleno+=1
      print

print("Cantidad de triangulos equilateros ->",equilatero)
print("Cantidad de triangulos isosceles ->",isosceles)
print("Cantidad de triangulos escaleno ->",escaleno)