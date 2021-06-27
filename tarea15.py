#Diseñe un pseudocódigo para calcular la suma y producto de 
#N números enteros, utilizando un bucle controlado por centinela."""

class Tarea15:
    def __init__ (self):
        pass
    def Variables(self):

        producto=1
        suma=0
        num=int(input("ingrese un numero entero que no sea negativo:"))
    
        while num != -1 :
            
            num=int(input("Ingrese un numero:"))
            suma=suma+num
            producto=producto*num
            
            print("""Total de la suma es:""",suma,"""Total del producto es: """,producto)
          
        input("enter para salir") 
resultado = Tarea15()
resultado.Variables()