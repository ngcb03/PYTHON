# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo 
# según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
# Nivel máximo: Porcentaje >= 90%
# Nivel medio: Porcentaje >=75% y <90%
# Nivel regular: Porcentaje >=50% y <90%
# Fuera de nivel: Porcentaje <50%

cantPreg = int(input("Ingresa cantidad de preguntas: "))
cantResp = int(input("Ingresa cantidad de respuestas: "))
porc=(cantResp*100)/cantPreg
print("¡Usted se encuentra dentro del nivel: ")
if porc>=90:
	print("máximo (>=90%)!")
if porc>=75:
	print("medio (>=75% y <90%)!")
if porc>=50:
	print("regular (>=50% y <75%)!")
else:
	print("bajo (<50%)!")
print("Porcentaje de acierto:",porc,"%")



