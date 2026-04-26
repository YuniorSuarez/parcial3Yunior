#fibonacci
# YuniorEstebanSuarezMozo
numeroDeIteraciones = int(input("Ingrese el numero de iteraciones: "))

i=0
j=1
 
for k in range(numeroDeIteraciones): 
    print("El numero de Fibonacci es: ", i)
    i, j = j, i + j  
    
    
    