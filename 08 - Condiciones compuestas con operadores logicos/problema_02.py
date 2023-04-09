# Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo)
# Cargar por teclado el valor numérico del día, mes y año. Ejemplo: dia:10 mes:2 año:2018

dia = int(input("Ingresa dia actual: "))
mes = int(input("Ingresa mes actual: "))
anio = int(input("Ingresa anio actual: "))
print("¡La fecha",dia,"/",mes,"/",anio)
if mes>0 and mes<4:
	print("SI")
else:
	print("NO")
print("corresponde al tercer trimestre!")
