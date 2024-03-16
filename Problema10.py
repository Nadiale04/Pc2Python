def mes_num(m):
    meses = {"Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"}
    return meses[m]

def fecha_AAA_MM_DD(f):
    mes_dia_anio = f.split()
    if '/' in f:
        mes, dia, anio = f.split('/')
    else:
        mes = mes_num(mes_dia_anio[0])
        dia = mes_dia_anio[1][:-1]
        anio = mes_dia_anio[2]
    return f"{anio}-{mes}-{dia:02}"

    
fecha_ingresada = input('Ingrese la fecha: ').title()
fecha_corregida =fecha_AAA_MM_DD(fecha_ingresada)
print(fecha_corregida)