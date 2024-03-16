def calcular_fact(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact

numeroingresado=int(input('Ingrese un número para calcular el factorial: '))
fact=calcular_fact(numeroingresado)

print(f'El factorial de {numeroingresado} es: {fact}')