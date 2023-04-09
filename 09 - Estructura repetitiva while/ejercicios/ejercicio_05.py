# Mostrar los múltiplos de 8 hasta el valor 500. 
# Debe aparecer en pantalla 8 - 16 - 24, etc.

contador=1
mult=0

while mult<=500:
  mult=8*contador
  print(mult)
  contador+=1