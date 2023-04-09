# Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter
# "@".

mail = input("Ingrese su e-mail: ")
f=0
arroba=0

while f<len(mail):
  if mail[f]=='@':
    arroba+=1
  f+=1

if arroba==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")

# Los string en Python son inmutables, esto quiere decir que una vez que los inicializamos 
# no podemos modificar su contenido:
nombre="juan"
nombre[0]="c" # Esto no se puede

# No hay que confundir cambiar parte del string con realizar la asignación de otro string a 
# la misma variable, luego si es correcto asignar otro valor a un string:

nombre="juan"
print(nombre)
nombre="ana"
print(nombre)