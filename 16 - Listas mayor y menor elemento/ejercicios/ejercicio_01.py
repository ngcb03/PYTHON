"""

Programador: Nicolas G. Camargo B.

Programa: Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético

Última modificación: 01-02-23

"""

listaPersonas = []

print("¡Registro personas!")
for n in range(5):
  print("Persona #",n+1)
  listaPersonas.append(input("Ingrese nombre: "))
  print()

nombreCorto = listaPersonas[0]
for x in range(1,5):
  if len(listaPersonas[x]) < len(nombreCorto):
    nombreCorto = listaPersonas[x]

print("Lista personas:",listaPersonas)
print("Persona nombre más corto:",nombreCorto)
