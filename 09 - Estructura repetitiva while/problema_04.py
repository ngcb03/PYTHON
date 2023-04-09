# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar # y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté 
# comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de 
# piezas aptas que hay en el lote.

contador=0
piezasApt=0
cantPiezas = int(input("Cuantas piezas cargara: "))
print()
while contador<cantPiezas:
  print("Perfil piezas #",(contador+1))
  longPieza = float(input("Ingrese la medida de la pieza: "))
  if longPieza>=1.2 and longPieza<=1.3:
    piezasApt+=1
  contador+=1  
  print()
print("La cantidad de piezas aptas son ",piezasApt)    