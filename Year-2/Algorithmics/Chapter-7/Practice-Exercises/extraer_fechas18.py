from sys import argv

meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]


with open(argv[1], 'r') as fichero:
    int_dias = []
    int_meses = []
    int_anyos = []

    for linea in fichero:
        fecha = linea.strip().split(" ")

        int_dias.append(int(fecha[0]))
        for posicion in range(len(meses)):
            if meses[posicion] == fecha[1]:
                int_meses.append(posicion)
        int_anyos.append(int(fecha[2]))

mayor_anyo = max(int_anyos)
menor_anyo = min(int_anyos)

dias_mayores = []
dias_menores = []
meses_mayores = []
meses_menores = []

for i in range(len(int_anyos)):
    if int_anyos[i] == mayor_anyo:
        dias_mayores.append(int_dias[i])
        meses_mayores.append(int_meses[i])
    if int_anyos[i] == menor_anyo:
        dias_menores.append(int_dias[i])
        meses_menores.append(int_meses[i])

mayor_mes = max(meses_mayores)
menor_mes = min(meses_menores)

dias_mayores2 = []
dias_menores2 = []

for i in range(len(meses_mayores)):
    if meses_mayores[i] == mayor_mes:
        dias_mayores2.append(dias_mayores[i])

for i in range(len(meses_menores)):
    if meses_menores[i] == menor_mes:
        dias_menores2.append(dias_menores[i])

mayor_dia = max(dias_mayores2)
menor_dia = min(dias_menores2)

print("La fecha más antigua es el", menor_dia, meses[menor_mes], menor_anyo)
print("La fecha más reciente es el", mayor_dia, meses[mayor_mes], mayor_anyo)


