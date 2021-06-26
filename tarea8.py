#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres
class tarea8:
    def __init__(self):
          pass
    def numero(self):
    
        
     print ("Mayor de 3 Números")
a = int(input("Ingrese el Num1: \n"))
b = int(input("Ingrese el Num2: \n"))
c = int(input("Ingrese el Num3: \n"))
if (a > b):
 mayor = a
else:
 mayor = b

if (c > mayor):
 mayor = c

print ("El Mayor de los 3 números es:", mayor)

           
tarea=tarea8()
tarea.numero()