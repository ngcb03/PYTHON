# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.
dia = int(input("Ingresa un dia valido: "))
mes = int(input("Ingresa un mes valido: "))
anio = int(input("Ingresa un anio valido: "))
if dia>0 and dia<32 and mes>0 and mes<13 and anio>0:
	print("!La fecha")
	if mes==12:
		print("SI")
	else:
		print("NO")
	print("corresponde a navidad!")
else:
	print("¡La fecha no es correcta!")
