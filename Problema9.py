def omitir_vocales(texto):
    vocales="aeiouAEIOU"
    for vocal in vocales:
        texto=texto.replace(vocal, "")
    return texto

texto_ingresado = input("Escriba un texto... ")

texto_acortado = omitir_vocales(texto_ingresado)

print(texto_acortado)