def contador (n,d):
    numero_cadena=str(n)
    cantidad_veces=numero_cadena.count(str(d))
    return cantidad_veces

numero_ingresado=int(input('Ingrese un número: '))
digito_ingresado=int(input('Ingrese un dígito: '))
cantidad_veces=contador(numero_ingresado,digito_ingresado)
print(f'La cantidad de veces {digito_ingresado} en el número es de: {cantidad_veces}')