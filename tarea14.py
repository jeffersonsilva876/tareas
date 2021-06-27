#Diseñe un pseudocódigo para calcular
#la suma y producto de N números enteros, 
#utilizando un bucle controlado por el usuario.."""

class Tarea14:
    def __init__ (self):
        pass
    def Variables(self):
        prod=1
        suma=0
        resp=input(str("Quieres ingresar numeros??  (S/N)"))
        while resp != "n" and resp!= "N":
            
            num=int(input("Ingrese un numero: "))
            suma=suma+num
            prod=prod*num
            resp=input(str("Desea continuar (S/N)"))
        print("""Total de la suma es:""",suma,"""
             Total del producto es: """,prod)
          
        input("enter para salir") 
        
resultado = Tarea14()
resultado.Variables()