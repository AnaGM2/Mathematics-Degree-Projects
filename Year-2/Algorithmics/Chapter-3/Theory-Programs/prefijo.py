# Programa que calcula el prefijo común más largo
# entre dos cadenas

# Sería más adecuado introducir el cálculo del prefijo en una función
# que recibiera dos cadenas como argumento y devolviera otra cadena con
# el prefijo común más largo

#Lectura de cadenas introducidas por el usuario
cad1=input("Dame la cadena 1: ")
cad2=input("Dame la cadena 2: ")

#Prefijo común más largo encontrado hasta el momento
prefijo=""

#Longitud del prefijo candidato que vamos a examinar
longitud_candidato=1

#Probaremos prefijos siempre que éstos no sean más largos que alguna de las dos cadenas
while longitud_candidato <= len(cad1)  and longitud_candidato <= len(cad2) :

    #Si los prefijos son iguales, actualizamos la variable "prefijo"
    if cad1[:longitud_candidato] == cad2[:longitud_candidato]:
        prefijo=cad1[:longitud_candidato]
    else:
        #Si no, interrumpimos el bucle para no realizar cáclulos innecesarios
        break
    longitud_candidato += 1


print(prefijo)
