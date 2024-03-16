listado=[]
for i in range(1500,2701):
     if i%7==0 and i%5==0:
          listado.append(i)
print(f'Los números divisibles por 7 y múltiplos de 5 son: {listado}')