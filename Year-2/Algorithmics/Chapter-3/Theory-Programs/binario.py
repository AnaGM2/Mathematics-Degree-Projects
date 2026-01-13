# Función que calcula el número entero correspondiente
# a un número binario según la representación posicional
# El número binario se encuentra codificado como una cadena de caracteres
def binario_a_entero(cad):
    resultado=0
    for i in range(0,len(cad)):
        if cad[-(i+1)] == '1':
            num =  2 ** i
            resultado+=num
    return resultado

#Pequeño programa principal para probar la función
print(binario_a_entero('01101'))
