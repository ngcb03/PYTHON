# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un
#  programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran 
# entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el 
# importe que gasta la empresa en sueldos al personal.

print()
nEmpleados=int(input("Ingresar cantidad de empleados a registrar: "))
print()

contador=0
sueldoMen=0
sueldoMay=0
sueldoGeneral=0

while contador<nEmpleados:
  print("Sueldo persona #1 ->")
  sueldo = int(input("Ingresar sueldo: "))
  print()
  if sueldo>=100 and sueldo<=500:
    if sueldo<=300:
      sueldoMay+=1
    else:
      sueldoMen+=1
    sueldoGeneral+=sueldo
    contador+=1
  else:
    print("¡Sueldo erroneo -> 100<=sueldo<=500!")  
    print()

print("Empleados con sueldo menor-igual a 300:",sueldoMay)    
print("Empleados con sueldo mayor a 300:",sueldoMen)
print("Ingresos generales empledos:",sueldoGeneral)
