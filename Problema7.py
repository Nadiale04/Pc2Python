def evaluar_primo(x):
    es_primo=True
    for i in range(2,x):
        if x%i==0:
            es_primo=False
            break 
    return es_primo

num_ingresado=int(input('Ingrese un número: '))
es_primo=evaluar_primo(x=num_ingresado)

if es_primo:
    print('El número es primo')
else:
    print('El número no es primo')