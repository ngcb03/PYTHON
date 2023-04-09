# Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza
# con vocal dicho nombre.

nomPersona = input("Ingrese su nombre: ").lower()
comVocal=0

if nomPersona[0]=='a' or nomPersona[0]=='e' or nomPersona[0]=='i' or nomPersona[0]=='o' or nomPersona[0]=='u':
  print("¡El nombre SI comienza por una vocal!")
else:
  print("¡El nombre NO comienza por una vocal!")
