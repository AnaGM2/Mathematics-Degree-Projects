# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:46:38 2024

@author: gilpe
"""


# EJERCICIO 3

def euclides(a, b):
    
    if b == 0:
        return (a, 1, 0)
    
    else:
        q = a // b
        r = a % b
        (mcd, u0, v0) = euclides(b, r)
        u = v0
        v = u0-q*v0
        return (mcd, u, v)
    
euclides(37,17)
    


# EJERCICIO 7

def inversa(a,m):
    v = euclides(a,m)[1]
    return v % m

inversa(2,25)



# EJERCICIO 11

def analisis_frecuencia(ciphertext):
    ciphertext = ciphertext.upper()
    
    frecuencias = {}
    for caracter in ciphertext:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    letra1 = frecuencias_ordenadas[0][0]
    letra2 = frecuencias_ordenadas[1][0]
    
    # A ----> letra1  <==>  0 ----> y1
    # E ----> letra2  <==>  4 ----> y2
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y1 = alfabeto.index(letra1)
    y2 = alfabeto.index(letra2)
            
    return y1, y2

ciphertext = ("ITFMGWTITJWARGIJGTRWGTFGLIPNIWJGFWLWABGOKWFWLGJWGGTFGLIPGCWAMJZMW"
        "JKTEGPBGOVKGTFGLIPYGLEGAOKCKLGOKCMFGNJMGYFMDWFWLMOGFGCWTRWGLCKPKFWLGOKP" 
        "MTGSIWSIWJMGSIWCWLGAMJZMWJGTOGLMWTRWYNMTGLCWTRWOMTAWEIMOKCMFGOGLMWTRW")
analisis_frecuencia(ciphertext)   
  

def cifra_afin(ciphertext,a,b):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a_inv = inversa(a,26)
    
    plaintext = ""
    for caracter in ciphertext:
        y = alfabeto.index(caracter)
        x = a_inv*(y-b) % 26
        plaintext = plaintext + alfabeto[x]
    return plaintext


a = 17
b = 6
cifra_afin(ciphertext, a, b)



# EJERCICIO 13

def Ic(x):
    x = x.lower()
    m = len(x)
    
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    frecuencias = {letra: 0 for letra in abecedario}
    for caracter in x:
        frecuencias[caracter] += 1
        
    Ic = 0
    for f in frecuencias.values():
        Ic += f*(f-1)/(m*(m-1))
    return Ic


def formar_subtextos(ciphertext, n):
    subtextos = []
    
    for i in range(n):
        y = ciphertext[i::n]
        subtextos.append(y)
    
    return subtextos


def MIc(x,y):
    x = x.lower()
    y = y.lower()
    m = len(x)
    t = len(y)
    
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    frecuenciasx = {letra: 0 for letra in abecedario}
    frecuenciasy = {letra: 0 for letra in abecedario}

    for caracter in x:
        frecuenciasx[caracter] += 1
    for caracter in y:
        frecuenciasy[caracter] += 1
        
    f = list(frecuenciasx.values())
    g = list(frecuenciasy.values())
    
    MIc = 0
    for i in range(26):
        MIc += f[i]*g[i]/(m*t)
    return MIc


def desplazamiento(y,g):
    y = y.lower()
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    y_g = ""
    for caracter in y:
        i = abecedario.index(caracter)
        y_g = y_g + abecedario[(i+g)%26]
    return(y_g)


def frecuencias(ciphertext,n=1):
    ciphertext = ciphertext.lower()
    if n == 1:
        abecedario = 'abcdefghijklmnopqrstuvwxyz'
        frecuencias = {letra: 0 for letra in abecedario}
        for caracter in ciphertext:
            frecuencias[caracter] += 1
    else:
        frecuencias = {}
        for i in range(0, len(ciphertext)):
            if len(ciphertext[i:i+n]) == n:
                if ciphertext[i:i+n] in frecuencias:
                    frecuencias[ciphertext[i:i+n]] += 1
                else:
                    frecuencias[ciphertext[i:i+n]] = 1  
        frecuencias = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    return frecuencias


def posiciones_grupo(ciphertext,grupo):
    ciphertext = ciphertext.lower()
    grupo = grupo.lower()
    posiciones=[]
    i = 0
    while i < len(ciphertext):
        indice = ciphertext.find(grupo,i)
        if indice == -1:
            break
        posiciones.append(indice)
        i = indice + 1
    return posiciones
        

ciphertext = ("Pwhkfqkvedwwkxospcogkmebwogfgghlstadblkadbmiooblkcugetrfwqviwmv"
              "yqlmrisszeihlkiifbxxuuuitnwfipmcuqxnavivkrhammbhlexcxvhicpxyzow"
              "qstoopexrqmwyovaysdwqstgpioobjayivdtkuflblsgkivjhrjvkonqrvfdkxo"
              "qhjcgbbihbsuaexmLbmyhkmsxswqggzogtugvqfrswwfxsdswaqkiwegwmqhiwq"
              "xoglvjkovqfrswwhugrjcgbbsrukqxvgqwqggzpmetgWpiysvklkahaexswpixs"
              "iwvkhhzqkrfwqviwixocqiprmvmgafhblkcumxoqdtejjdvgkghomsduwzkahvx"
              "ywqqrzsjmvlofbsxwcixocqipmcuqxnavirjtdaxkffwqviwqrmhhkltcowkefh"
              "yyofhblkghasriwqstgwwfkqrvxobxiprmdlevhhlXnsumidwvbmttrzqghlwrz"
              "vhwvkhlkerzbaiiiumwivhuiyhkixvfrdehzbketbrbfkpuwokbhditklblaboq"
              "qohhlguascxobjxscsuirkldutrslaxnsrvizwpmtgrecxzvhaiyqkmqkgdzisc"
              "umhotiqgazwbsoastissqbxnoqblkphaxzvhwvkhlkerzbjvkonifrsecxicpxy"
              "zowqstootcysfcvkahklgblaqy")

frec3 = frecuencias(ciphertext,3)
posiciones_grupo(ciphertext,"blk")
posiciones_grupo(ciphertext,"wqs")
posiciones_grupo(ciphertext,"qst")

n = 5
resultado = formar_subtextos(ciphertext, n)

for y in resultado:
    print(Ic(y))

y1 = resultado[0]
y2 = resultado[1]
y3 = resultado[2]
y4 = resultado[3]
y5 = resultado[4]

frecuencias(y1)
# Suponemos T ---> W
# 19+k1 = 22
k1 = 3

for g in range(0,26):
    y2_g = desplazamiento(y2,g)
    print(g,":",MIc(y1,y2_g))  
# k1-k2 = g2 = 21
k2 = 8

for g in range(0,26):
    y3_g = desplazamiento(y3,g)
    print(g,":",MIc(y1,y3_g)) 
# k1-k3 = g3 = 25
k3 = 4

for g in range(0,26):
    y4_g = desplazamiento(y4,g)
    print(g,":",MIc(y1,y4_g)) 
# k1-k4 = g4 = 23
k4 = 6 

for g in range(0,26):
    y5_g = desplazamiento(y5,g)
    print(g,":",MIc(y1,y5_g)) 
# k1-k5 = g5= 15
k5 = 14

abecedario = 'abcdefghijklmnopqrstuvwxyz'
plaintext = ""
j = 1
for caracter in ciphertext:
    i = abecedario.index(caracter.lower())
    if j == 1:
        plaintext += abecedario[(i-k1)%26]
        j += 1
    elif j == 2:
        plaintext += abecedario[(i-k2)%26]
        j += 1
    elif j == 3:
        plaintext += abecedario[(i-k3)%26]
        j += 1
    elif j == 4:
        plaintext += abecedario[(i-k4)%26]
        j += 1
    elif j == 5:
        plaintext += abecedario[(i-k5)%26]
        j = 1
print(plaintext)

# clave = "DIEGO"



# EJERCICIO 15

ciphertext = ("Scrhxbquedhrmfosnmwvnsoyozmeggsgubadzvspghwfgzhkkcfbgbrfuadxzsfv"
              "iwsqisdugqhlisquedhrmfosnwqdrucuohvpyofhjsglmbsggfcxtrqrsdiwghwr"
              "tozkgfrqkggdygipvhwrtgadqwbjyiqkgzurxwhksgvdxrhrhfsdqwbsxoqwoqse"
              "eobbgrjhxgoueWhlyhvhufswoqoormdrygwershrhfsdqgifnogbyhsphihlzwgl"
              "ttsdywpokhcgugceeobbqbcztdfdihwfgzahgbgWnsghyqvhssgdxshkkfsiufsw"
              "kfahjqcpvihdzwcqgzzbysqxxshkkcfhzwqdrorygbqhysulsdfrbsahthgltwbw"
              "kusuloqwufwcghwrtozjufwwnagdtrtdyhsuicasahwqmhsfnbcouumukeilxshk"
              "kgsvuziwocbvzcphicbwobidrzmdjodwkrHkkfshdwgwobtrxaowocbwnscukhwf"
              "gzzbysqxxsgfnsahyhvdzdfrbopoeqoqtchekpfrqsbhbsbzohvxtzwpohsgicas"
              "ahwqmdczkfoqklopvzslyhvhubswoassgrpxzhvhysgfnsahyofhscfhjwtioqio"
              "zhclsdzhssbwzvoqzvsekghwnscukhwfgzzbhfsdqopokpiwicasahowocbdrzmvkqiukasfnoblyag")

n = 4
resultado = formar_subtextos(ciphertext, n)

for y in resultado:
    print(Ic(y))
    
y1 = resultado[0]
y2 = resultado[1]
y3 = resultado[2]
y4 = resultado[3]


for g in range(0,26):
    y2_g = desplazamiento(y2,g)
    print(g,":",MIc(y1,y2_g))   
g2 = 18

for g in range(0,26):
    y3_g = desplazamiento(y3,g)
    print(g,":",MIc(y1,y3_g))  
g3 = 18

for g in range(0,26):
    y4_g = desplazamiento(y4,g)
    print(g,":",MIc(y1,y4_g))    
g4 = 3

# k1-k2 = 18  <==>  k2 = k1+8
# k1-k3 = 18  <==>  k3 = k1+8
# k1-k4 = 3   <==>  k4 = k1+23

abecedario = 'abcdefghijklmnopqrstuvwxyz'

for k1 in range(26):
    k2 = (k1+8)%26
    k3 = (k1+8)%26
    k4 = (k1+23)%26
    plaintext = ""
    j = 1
    for caracter in ciphertext:
        i = abecedario.index(caracter.lower())
        if j == 1:
            plaintext += abecedario[(i-k1)%26]
            j += 1
        elif j == 2:
            plaintext += abecedario[(i-k2)%26]
            j += 1
        elif j == 3:
            plaintext += abecedario[(i-k3)%26]
            j += 1
        elif j == 4:
            plaintext += abecedario[(i-k4)%26]
            j = 1
    print(k1,":",plaintext)
        
# k1 = 6
# k2 = 6+8 = 14
# k3 = 6+8 = 14
# k4 = 6+23 = 3

# clave = "GOOD" 



# EJERCICIO 19

def LFSR(semilla):
    secuencia = semilla.copy()
    secuencia.append((semilla[0] + semilla[1])%2)
    i=1
    while secuencia[i:] != semilla:
        secuencia.append((secuencia[i] + secuencia[i+1])%2)
        i += 1
    return secuencia
    
    
semilla = [1,0,0,0]
LFSR(semilla)
