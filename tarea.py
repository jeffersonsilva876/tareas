#Una escuela aplica dos exámenes a sus aspirantes, por lo 
#que cada uno de ellos obtiene dos calificaciones denotadas
#como C1 y C2. El aspirante que obtenga una calificación mayor
#que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado
class Tarea11:
    def __init__ (self):
        pass
    def Variables(self):
        
        C1= float(input("Ingrese primer Calificacion: "))
        C2= float(input("Ingrese segunda Calificacion: "))
        
        if C1>=90 or C2>=90:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("aceptado",)
        else:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("denegado")
            
resultado = Tarea11()
resultado.Variables()