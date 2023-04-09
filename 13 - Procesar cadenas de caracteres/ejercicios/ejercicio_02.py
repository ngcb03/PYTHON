# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar 
# la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para 
# que sea más fácil disponer la condición que verifica que es una vocal.

oracion = input("Ingrese oración: ")
oracion = oracion.lower()
contVoc = 0 # contados de vocales en la oración

for f in oracion:
  if f=='a' or f=='e' or f=='i' or f=='o' or f=='u':
    contVoc+=1

print("Cantidad de vocales en la oración:",contVoc)