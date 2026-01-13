class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def iniciales(self):
        cadena = ''
        for caracter in self.nombre:
            if caracter in 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ':
                cadena = cadena + caracter + '. '
        return cadena

    def __str__(self):
        cadena = 'Nombre: {0}\n'.format(self.nombre)
        cadena = cadena + 'DNI: {0}\n'.format(self.dni)
        cadena = cadena + 'Edad: {0}\n'.format(self.edad)
        return cadena

    def copia(self):
        nuevo = Persona(self.nombre[:], self.dni[:], self.edad)
        return nuevo


toni = Persona('Antonio Perez', '234534432Y', 20)
print(toni.edad)
print(toni.iniciales())
print(toni)
copia = toni.copia()
copia.dni = '123456789Z'
print(copia.dni)
print(toni.dni)
