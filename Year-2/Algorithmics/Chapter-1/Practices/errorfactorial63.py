num = int(input('Introduce un entero: '))

fact = 0
for i in range(num, 2, -1):
    fact = fact * i

print('El factorial de ', num, ' es ', fact)

# El error es que inicialmente fact=0, por lo que al multiplicarlo por cada i sigue dando 0.
