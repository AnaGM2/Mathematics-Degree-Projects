from sys import argv, stderr

intentos = 3

while intentos > 0:
    with open(argv[1], 'r') as fichero:
        incorrecto = True
        email = input("Introduce tu email: ")
        contrasena = input("Introduce tu contraseña: ")
        datos = email + ":" + contrasena
        for linea in fichero:
            if linea.strip() == datos:
                print("Datos correctos, acceso permitido")
                incorrecto = False
                intentos = 0
                break
        if incorrecto:
            intentos -= 1
            if intentos == 0:
                print("Datos incorrectos, demasiados intentos. Acceso denegado", file=stderr)
            else:
                print("Datos incorrectos, vuelve a intentarlo")
