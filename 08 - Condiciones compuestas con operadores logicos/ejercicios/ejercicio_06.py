# De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un 
# programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, 
# otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un 
# aumento de 5 %.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

aumento = 0
sueldo = int(input("Ingresar sueldo operario: "))
antiguedad = int(input("Ingresa antiguedad del operario: "))
if sueldo<500:
  if antiguedad>=10:
    aumento=(sueldo*20)/100
  else:
    aumento=(sueldo*5)/100

print("Sueldo operario -> ",(sueldo+aumento))