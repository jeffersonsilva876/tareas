#Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
class tarea5:
    def __init__(self):
        pass
    def Calcular(self):
       
        cal=float(input("Ingrese su calificacion:"))
        if cal >= 7 :
            print()
            print("usted ha aprobado")
            print("APROBADO")
        else:
            print()
            print("usted ha reprobado")
            print("REPROBADO")
        print()
       
        input("fin")

tarea = tarea5()
tarea.Calcular()