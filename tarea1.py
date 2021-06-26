#En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera.

def run():
    pi=3.1416
    R =int(input("Ingrese el Radio del circulo : "))
    
    cal =R*R
    S=cal*pi
    print("La superficie del circulo es: ")
    print(S)
    
class Tarea1:
    def __init__(self):
        pass
    def Calcular(self):
        pi=3.1416
        R =int(input("Ingrese el Radio del circulo : "))
        
        cal =R*R
        S=cal*pi
        print("La superficie del circulo es: ")
        print(S)
        
    
if __name__ == "__main__":
    run() 
tarea= Tarea1()
tarea.Calcular() 