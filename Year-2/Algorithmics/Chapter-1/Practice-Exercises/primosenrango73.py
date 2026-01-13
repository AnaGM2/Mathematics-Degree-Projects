a = int(input("Introduce un número entero: "))
b = int(input("Introduce otro número entero mayor que el anterior: "))

for num in range(a, b+1):
    primo = True
    for div in range(2, num):
        if num % div == 0:
            primo = False
            break
    if primo:
        print(num)
