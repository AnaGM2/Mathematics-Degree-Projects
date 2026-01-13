a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

try:
    x = -b / a
    print('Solución: ', x)
    if x < 0:
        raise ValueError

except ZeroDivisionError:
    print('La ecuación no tiene solución')

except ValueError:
    print('La solución es negativa')
