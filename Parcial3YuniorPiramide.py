#Piramide
# Yunior Esteban Suarez Mozo
numeroDeFilas = int(input("Ingrese el numero de filas: "))

for fila in range(1, numeroDeFilas + 1):
    print()
    for columna in range(1,fila + 1):
        print(f"{columna}", end=" ")
        