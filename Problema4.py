alumnos = []

while True:
    respuesta = input('¿Desea ingresar notas?: ').upper()
    if respuesta == 'SI':
        nombre_alumno = input('Ingrese el nombre del alumno: ').title()

        notas_alumno = []
        for nota in range(3):
            nota_ingresada = float(input(f"Ingrese la calificación {nota+1}: "))
            notas_alumno.append(nota_ingresada)
        alumno = {'Alumno': nombre_alumno, 'Notas': notas_alumno}
        alumnos.append(alumno)

    elif respuesta == 'NO':
        break
    else:
        print("Respuesta inválida. Por favor, ingrese 'SI' o 'NO'.")

print("Listado de Alumnos y Notas:")
for x in alumnos:
    print(f"Alumno: {x['Alumno']}, Notas: {x['Notas']}")
