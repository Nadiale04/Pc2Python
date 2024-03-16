def fibonacci(x):
    x1, x2 = 0, 1
    serie = [x1]
    while x2 <= x:
        serie.append(x2)
        x1, x2 = x2, x1 + x2
    return serie

serie = fibonacci(50)
print(f'La secuencia de Fibonacci es la serie de números: {serie}')