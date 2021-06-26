#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:
class entero:
    def __init__(self):
          pass
    def entero(self):
      print("-------------------------------------------------------")
print(" FUNCIÓN.")
print("-------------------------------------------------------")

print("Ingrese valores: ")
NUM = int( input("Tipo de Calculo: "))
V = int( input("Ingrese V:"))

Funcion = {
1 : 100*V,
2 : 100**V,
3 : 100/V
}

VAL = Funcion.get(NUM, 0)
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(VAL)
 
variable=entero()
variable.entero()