# Ecribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al # comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

n = int(input("Cantidad de coordenadas a registrar -> "))

for f in range(n):
  print("Coordenada #",f+1)
  x = int(input("Ingrese coordenada en x -> "))
  y = int(input("Ingrese coordenada en y -> "))
  
  if x!=0 and y!=0:
    if x>0:
      if y>0:
        print("¡Cuadrante I!")
      else:
        print("¡Cuadrante IV!")
    else:
      if y>0:
        print("¡Cuadrante II!")
      else:
        print("¡Cuadrante III!")
  else: 
    print("¡Cuadrante neutro!")
  print()  