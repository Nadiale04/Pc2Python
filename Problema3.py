listadenumeros=[]
numeros_pares=0
numeros_impares=0

while True:
    opcion=input('¿Desea ingresar un número? ').upper()
    if opcion=='SI':
        numeros_ingresados=int(input('Ingrese el número: '))
        listadenumeros.append(numeros_ingresados)
        if numeros_ingresados%2==0:
            numeros_pares+=1
        else:
            numeros_impares+=1
    elif opcion=='NO':
        break
    else:
        print('Opción inválida, intenta denuevo') 

print(f'Números ingresados: {listadenumeros}')
print(f'Cantidad de números pares: {numeros_pares}')
print(f'Cantidad de números impares: {numeros_impares}')