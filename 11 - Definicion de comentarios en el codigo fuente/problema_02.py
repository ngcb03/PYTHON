# Mostrar la tabla de multiplicar del 5 empleando primero el while y seguidamente de nuevo 
# empleando el for.

# Contador que sirve para recorrer/incrementar hasta el límite solicitado
cont=0

# Uso del bucle while
print("Bucle While ->")
while cont<=50: # Condición de límite
  print(cont)
  cont+=5 # Contador avanza

print()

# Uso del bucle for
print("Bucle For ->")
for f in range(5,51,5): # f como variable que recorre lista con incre de 5
  print(f)