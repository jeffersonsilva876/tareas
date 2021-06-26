#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class tarea6:
    def __init__(self):
        pass
    def Calcular(self):
        SUELDO=float(input("Sueldo de empleados:"))
        if SUELDO < 600:
            NS=SUELDO + SUELDO*0.1
            print()
        else:
            NS=SUELDO
            print()
        print(NS)
        
        input("fin")
tarea=tarea6()
tarea.Calcular()