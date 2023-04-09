# Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir 
# dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante # si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

sectorCor = 0
corX = int(input("Ingresa la coordenada x -> "))
corY = int(input("Ingresa la coordenada y -> "))
if corX!=0:
  if corX>0:
    sectorCor+=1
  else:
    sectorCor-=1
if corY!=0:
  if corY>0:
    if sectorCor==(-1):
      sectorCor+=2
    else:
      sectorCor+=1  
  else:
    if sectorCor==1:
      sectorCor-=2
    else:
      sectorCor-=1  

print(sectorCor)

if sectorCor!=0:
  if sectorCor>0:
    if sectorCor==1:
      print("¡Cuadrante #2 -> [",corX,",",corY,"]!")  
    else:
      print("¡Cuadrante #1 -> [",corX,",",corY,"]!")
  else:
    if sectorCor==(-1):
      print("¡Cuadrante #4 -> [",corX,",",corY,"]!")
    else:
      print("¡Cuadrante #3 -> [",corX,",",corY,"]!")              
else:
  print("¡Cuadrante neutral -> [0,0]!")