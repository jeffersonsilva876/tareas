#Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.
        
j = 1
k = 1

while j <= 20:
    n = int(input(f"Ingrese un numero {j}: "))
    if n == 0:
        k = k +1
    else:
        if n < 0:
             j = j + 1
        else:
            k= k + 1
            
    j += 1
print(f"{j} numeros son negativos")
print(f"{k} numeros son positivos")
