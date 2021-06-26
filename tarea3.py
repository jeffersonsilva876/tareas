#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

class tarea3:
    def __init__(self):
        pass
    def Calcular(self):
        print("________________________________")
        SB=float(input("Ingrese Salario Base:"))
        V1=float(input("Ingrese valor venta 1:"))
        V2=float(input("Ingrese valor venta 2:"))
        V3=float(input("Ingrese valor venta 3:"))
        TV=V1+V2+V3
        C=TV*0.1
        TR=SB+C
        print()
        print("Su Total a Recibir es: ")
        print("$",TR)
        
        
tarea= tarea3()
tarea.Calcular()
