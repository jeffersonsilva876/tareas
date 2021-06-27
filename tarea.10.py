#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

class Tarea10:
    def __init__ (self):
        pass
    def Variables(self):
        
        i=1
        suma=0
        x=range(100)
        for i in x:
            suma=suma+i*i
            print("Suma: ",suma)
        
        input("fin")    

resul= Tarea10()
resul.Variables()