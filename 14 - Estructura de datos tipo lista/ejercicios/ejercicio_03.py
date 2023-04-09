# Definir una lista que almacene por asignación los nombres de 5 personas. 
# Contar cuantos de esos nombres tienen 5 o más caracteres.

listaNombres = ['camila','lorena','laura','lina','maria']
may = 0 # Contador nombres >= 5 caracteres

for f in listaNombres:
  if len(f)>=5:
    may+=1

print("Nombres >= 5 caracteres:",may)