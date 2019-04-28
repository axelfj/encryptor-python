#----------------------------------------------------------------------------#

#Funcion para eliminar tildes y mayusculas
def eliminartildes (texto):
    lista = ["á","é","í","ó","ú","ü"]
    lista2 = ["a","e","i","o","u","u"]
    texto = texto.lower()
    for x in texto:
        if x in lista:
            posicion = lista.index(x)
            texto = texto.replace(x,lista2[posicion])
    return texto
#----------------------------------------------------------------------------#
#Transposicion Codificacion

#Descripcion: Crear un programa al que se le cambie el orden (invertirlo) a un
#texto que ya ha sido asignado previamente
#Entradas: Sus entradas son un texto
#Salidas: Sus salidas son el texto invertido
#Restricciones: Algunas de las restricciones son que el texto no debe tener
#tildes, al igual que no puede tener mayusculas
 

def transposicionCod(texto):
    texto = eliminartildes(texto)
    if isinstance (texto, str):
        return texto[::-1]
    else:
        return "Debe ser un string"
    

#----------------------------------------------------------------------------#
#Transposicion Decodificacion

#Descripcion: Crear un programa al que se le cambie el orden que fue invertido
#previamente y que su resultado sea el original
#Entradas: Sus entradas son un texto codificado por transposicion previamente
#Salidas: Sus salidas son el texto original, decodificado
#Restricciones: Algunas de las restricciones son que el texto debe haber
#codificado previamente
    
def transposicionDec(texto):
    texto = eliminartildes(texto)
    if isinstance (texto, str):
        return texto[::-1]
    else:
        return "Debe ser un string"
    

#----------------------------------------------------------------------------#
#Cesar Codificacion
#Descripción: Crear un programa que convierta un texto a otro aplicando
#un desplazamiento dado por el usuario.
#Entradas: Sus entradas son un texto a codificar y un desplazamiento
#este desplazamiento, es puesto por el usuario.
#Salidas: Su salida es el texto codificado, aplicando el desplazamiento.
#Restricciones: Su principal restricción es que el desplazamiento
#no puede ser mayor a 27.

def cesarCod(texto, desplazamiento):
    if isinstance (texto, str):
        if isinstance (desplazamiento, int) and 27 >= desplazamiento and 0<desplazamiento:
            texto=eliminartildes(texto)
            abc = 'abcdefghijklmnñopqrstuvwxyz' + 'abcdefghijklmnñopqrstuvwxyz' 
            lista1=[i for i in texto]
            for j in lista1:
                pos = abc.find(j)
                if pos >= 0:
                    texto = texto.replace(j,abc[pos+desplazamiento])
            return texto
        else:
            return "Ingrese desplazamiento del 1 al 27"
    else:
        return "Debe ser un string"
        

#----------------------------------------------------------------------------#
#Cesar Decodificacion

#Descripción: Programa que nos devuelve un texto codificado.
#Entradas: Recibe por entradas el texto a codificar y el desplazamiento.
#Salidas: Nos da como resultado un texto codificado.
#Restricciones: El texto no puede ser escrito en mayúsculas.

def cesarDec(texto, desplazamiento):
    if isinstance (texto, str):
        if isinstance (desplazamiento, int) and 27 >= desplazamiento and 0<desplazamiento:
            texto=eliminartildes(texto)
            abc = 'abcdefghijklmnñopqrstuvwxyz' + 'abcdefghijklmnñopqrstuvwxyz' 
            lista2=[i for i in texto]
            for j in lista2:
                pos = abc.find(j)
                if pos >= 0:
                    texto = texto.replace(j,abc[pos-desplazamiento])
            return texto
        else:
            return "Ingrese desplazamiento del 1 al 27" 
    else:
        return "Debe ser un string"


#----------------------------------------------------------------------------#
#Codificacion Binaria

#Descripcion: Crear un programa en el cual en cada letra se le asigne un codigo
#(codigo binario) y devuelva el texto en binario
#Entradas: Sus entradas son un texto
#Salidas: Sus salidas son el texto en binario
#Restricciones: Algunas de las restricciones son que el texto no debe tener
#tildes, al igual que no puede tener mayusculas

a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z, _ = \
"00000", "00001", "00010", "00011", "00100", "00101", "00110", \
"00111", "01000", "01001", "01010", "01011", "01100", "01101", \
"01110", "01111", "10000", "10001", "10010", "10011", "10100", \
"10101", "10110", "10111", "11000", "11001", "11010", " * "

abc_bin = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z, _) 
abc = ('abcdefghijklmnñopqrstuvwxyz ')
abc = list(abc)

def binarioCod (texto):
    
    texto = eliminartildes(texto)
    lista = []
    texto = list(texto)
    for i in range(len(texto)):            
        for j  in range(len(abc)):           
            if abc[j] in texto[i]:         
                lista.append(abc_bin[j])     
    str = "".join(lista)
    return str




#----------------------------------------------------------------------------#
#Decodificacion Binaria

#Descripcion: Crear un programa en el cual un texto que ya fue codificado
#previamente en binario se pueda decodificar y que este en letras del abecedario
#Entradas: Sus entradas son un texto codificado de manera binaria previamente
#Salidas: Sus salidas son el texto original, decodificado
#Restricciones: Algunas de las restricciones son que el texto debe haber
#codificado previamente


def binarioDec(texto):
    abc = ['a', 'b','c','d' ,'e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    abcBin = ['00000','00001','00010','00011','00100', '00101', '00110','00111','01000','01001','01010','01011','01100','01101','01110','01111','10000','10001','10010','10011','10100','10101','10110','10111','11000','11001','11010', '*']
    texto = texto.split(" ")
    longtexto = len(texto)
    textocodificado = " "
    for i in texto:
        posicion = abcBin.index(i)
        nuevo = abc[posicion]
        textocodificado += nuevo
    else:
        print(textocodificado)

#----------------------------------------------------------------------------#
#Codificacion Leet

#Descripcion: Crear un programa en el cual en cada letra se le asigne un codigo
#o una manera diferente de llamarla y el resultado del texto sea en las nuevas
#variables a cada letra
#Entradas: Sus entradas son un texto
#Salidas: Sus salidas son el texto en las nuevas variables
#Restricciones: Algunas de las restricciones son que el texto no debe tener
#tildes, al igual que no puede tener mayusculas

a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z, _ = \
"4", "]3", "(", "[)", "[-", "(=", "(_+", \
")-(", "!", "_)", "⎜X", "1", "(V)", "]\[", \
"ñ", "()", "⎜*", "(,)", "I2", "$", "+", \
"[_]", "\\//", "\X/", ")(", "`/", "7_", " * "

abc_leet = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z, _) 
abc = ('abcdefghijklmnñopqrstuvwxyz ')
abc = list(abc)

def leetCod (palabra):
    
    palabra = eliminartildes(palabra)
    lista = []
    palabra = list(palabra)
    for i in range(len(palabra)):            
        for j  in range(len(abc)):           
            if abc[j] in palabra[i]:         
                 lista.append(abc_leet[j])     
    str = "".join(lista)
    return str
    


#----------------------------------------------------------------------------#
#Codificacion Monoalfabetico

#Descripcion: Crear un programa en el cual en cada letra se le asigne otra letra
#del abecedario a partir de una palabra clave ingresada por la persona
#Entradas: Sus entradas son un texto y la palabra clave
#Salidas: Sus salidas son el texto con los nuevos valores de cada letra
#Restricciones: Algunas de las restricciones son que el texto no debe tener
#tildes, al igual que no puede tener mayusculas

def monoCod (texto,palabra):
    if isinstance (texto, str) and (palabra, str):
        palabra = eliminartildes(palabra)
        texto = eliminartildes(texto)
        lista1=list(palabra)
        lista2=[]
        [lista2.append(x)for x in lista1 if x not in lista2]
        abc = "abcdefghijklmnñopqrstuvwxyz"
        [lista2.append(x) for x in abc if x not in lista2]
        resultado = []
        for x in texto:
                posicion = abc.find(x)
                if posicion >= 0:
                        resultado.append(lista2[posicion])
                else:
                    resultado.append(x)
        resultado = ''.join(resultado)
        return resultado
    else:
        return "Deben ser strings"


#----------------------------------------------------------------------------#
#Decodificacion Monoalfabetico

#Descripcion: Crear un programa en el cual se devuelva a un texto en abecedario
#normal por uno que habia sido codificado previamente con una palabra clave que
#cambia los valores de cada letra por otras letras del abecedario
#Entradas: Sus entradas son el texto codificado y la palabra clave
#Salidas: Sus salidas son el texto descodificado
#Restricciones: Algunas de las restricciones son que el texto debe estar
#codificado

def monoDec (texto,palabra):
    if isinstance (texto, str) and (palabra, str):
        palabra = eliminartildes(palabra)
        texto = eliminartildes(texto)
        lista1=list(palabra)
        lista2 = []
        [lista2.append(x)for x in lista1 if x not in lista2]
        abc = "abcdefghijklmnñopqrstuvwxyz"
        [lista2.append(x) for x in abc if x not in lista2]
        resultado = []
        lista2 = "".join(lista2)
        for x in texto:
                posicion = lista2.find(x)
                if posicion >= 0:
                        resultado.append(abc[posicion])
                else:
                    resultado.append(x)
        resultado = ''.join(resultado)
        return resultado
    else:
        return "Deben ser strings"



#----------------------------------------------------------------------------#
#Codificacion Vigenere

#Descripcion: Crear un programa en el cual en cada letra se le asigne otra letra
#del abecedario por medio de una palabra clave ya que cada letra del 
#abecedario tiene un valor y el de la palabra clave comparte los mismos valores
#que el abecedario, y la forma de codificarlo es sumar los valores de las letras
#del texto con los valores de las letras de la palabra clave, esto va a dar
#un nuevo valor que va a corresponder a la nueva letra
#Entradas: Sus entradas son un texto y la palabra clave
#Salidas: Sus salidas son el texto con los nuevos valores de cada letra
#Restricciones: Algunas de las restricciones son que el texto no debe tener
#tildes, al igual que no puede tener mayusculas



def vigenereCod(texto,palabra):
    if isinstance (texto, str) and (palabra, str):
        palabra = eliminartildes(palabra)
        texto = eliminartildes(texto)
        abc = "abcdefghijklmnñopqrstuvwxyz"
        resultado = ""
        i = 0
        for k in texto:
            if k not in abc:
                resultado+=k
            else:
                letra=i%len(palabra)
                letra2=palabra[letra]
                suma= abc.find(k)+abc.find(letra2)
                modulo = (suma % 27)
                resultado = resultado + abc[modulo]
                i += 1
        resultado =''.join(resultado)
        return resultado
    else:
        return "Deben ser strings"


#----------------------------------------------------------------------------#
#Decodificacion Vigenere

#Descripcion: Crear un programa en el cual se devuelva a un texto en abecedario
#normal por uno que habia sido codificado previamente con una palabra clave que
#cambia los valores de cada letra por otras letras del abecedario
#Entradas: Sus entradas son el texto codificado y la palabra clave
#Salidas: Sus salidas son el texto descodificado
#Restricciones: Algunas de las restricciones son que el texto debe estar
#codificado

def vigenereDec(texto,palabra):
    if isinstance (texto, str) and (palabra, str):
        texto = eliminartildes(texto)
        palabra = eliminartildes(palabra)
        abc = "abcdefghijklmnñopqrstuvwxyz"
        resultado = ""
        i = 0
        for k in texto:
            if k not in abc:
                resultado+=k
            else:
                letra=i%len(palabra)
                letra2=palabra[letra]
                suma= abc.find(k)-abc.find(letra2)
                modulo = (suma % 27)
                resultado = resultado + abc[modulo]
                i += 1
        resultado =''.join(resultado)
        return (resultado)
    else:
        return "Deben ser strings"

#----------------------------------------------------------------------------#

#Codificacion Fairplay#

#Descripción: Crea un programa el cual devuelve un texto codificado
#utilizando una palabra clave.
#Entradas: El programa recibe las entradas 'texto' y 'palabra'
#el texto es lo que se va a codificar y la palabra, es la palabra clave.
#Salidas: El texto codificado.
#Restricciones: Las dos entradas deben ser strings.

abecedario = ['a','b','c','d','e','f','g','h','i','j','k',\
             'l','m','n','ñ','o','p','q','r','s','t','u',\
             'v','w','x','y','z']

def playfairCod (texto,palabra):
    texto = eliminartildes(texto)
    palabra = eliminartildes(palabra)
    if isinstance (texto, str) and (palabra, str):
        matriz = [[],[],[],[],[],[]]
        abc = list(palabra)
        m = 0
        texto = list(texto)
        for i in abecedario:
            if i not in abc:
                abc.append(i)
        abc.append("1")
        abc.append("2")
        abc.append("3")
        for i in matriz:
            for j in range(5):
                i.append(abc[m])
                m += 1
        
        listexto = [texto[0]]
        for i in range(1,len(texto)):
            if texto[i] in abecedario:
                if texto[i-1] == texto[i]:
                    listexto.append('1')
                listexto.append(texto[i])

        if len(listexto)%2==1:
            listexto.append('1')
            
        listaTextoPares = [listexto[i:i+2] for i in range(0, len(listexto), 2)]

        textoFinal = ''
        
        for letras in listaTextoPares:
            indicesLetra1 = indicesMatriz(matriz,letras[0])
            indicesLetra2 = indicesMatriz(matriz,letras[1])
            
            if indicesLetra1[0] != indicesLetra2[0] and indicesLetra1[1] != indicesLetra2[1]:
                textoFinal += matriz[indicesLetra1[0]][indicesLetra2[1]]
                textoFinal += matriz[indicesLetra2[0]][indicesLetra1[1]]
            elif indicesLetra1[0] == indicesLetra2[0] and indicesLetra1[1] != indicesLetra2[1]:
                if indicesLetra1[1] + 1 > 4:
                    textoFinal += matriz[indicesLetra1[0] + 1][0]
                else:
                    textoFinal += matriz[indicesLetra1[0]][indicesLetra1[1] + 1]
                if indicesLetra2[1] + 1 > 4:
                    textoFinal += matriz[indicesLetra2[0] + 1][0]
                else:
                    textoFinal += matriz[indicesLetra2[0]][indicesLetra2[1] + 1]
            elif indicesLetra1[0] != indicesLetra2[0] and indicesLetra1[1] == indicesLetra2[1]:
                if indicesLetra1[0] + 1 > 5:
                    textoFinal += matriz[0][indicesLetra1[1] + 1]
                else:
                    textoFinal += matriz[indicesLetra1[0] + 1][indicesLetra1[1]]
                if indicesLetra2[0] + 1 > 5:
                    textoFinal += matriz[0][indicesLetra2[1] + 1]
                else:
                    textoFinal += matriz[indicesLetra2[0] + 1][indicesLetra2[1]]
        textoFinal = ''.join(textoFinal) 
        return textoFinal        
    else:
        return "Deben ser strings"


def indicesMatriz(matriz,letra):
    indices = []
    for fila in matriz:
        if  letra in fila:
            indices.append(matriz.index(fila))
            indices.append(fila.index(letra))
    
    return indices

#----------------------------------------------------------------------------#

#Decodificacion Playfair

#Descripción: Programa capaz de descodificar un texto codificado en playfair.
#Entradas: Recibe el texto codificado y la misma palabra clave que se uso
#para codificar el texto.
#Salidas: Nos resulta un texto descodificado.
#Restricciones: El texto que se introduce debe estar codificado y la palabra
#clave que se utiliza debe ser la misma que se uso para codificarlo.

abecedario = ['a','b','c','d','e','f','g','h','i','j','k',\
             'l','m','n','ñ','o','p','q','r','s','t','u',\
             'v','w','x','y','z']

def playfairDec (texto,palabra):
    if isinstance (texto, str) and (palabra, str):
        matriz = [[],[],[],[],[],[]]
        abc = list(palabra)
        m = 0
        texto = list(texto)
        for i in abecedario:
            if i not in abc:
                abc.append(i)
        abc.append("1")
        abc.append("2")
        abc.append("3")
        for i in matriz:
            for j in range(5):
                i.append(abc[m])
                m += 1
        
        listexto = [texto[0]]
        for i in range(1,len(texto)):
            if texto[i] in abecedario:
                if texto[i-1] == texto[i]:
                    listexto.append('1')
                listexto.append(texto[i])

        if len(listexto)%2==1:
            listexto.append('1')
            
        listaTextoPares = [listexto[i:i+2] for i in range(0, len(listexto), 2)]

        textoFinal = ''
        
        for letras in listaTextoPares:
            indicesLetra1 = indicesMatriz(matriz,letras[0])
            indicesLetra2 = indicesMatriz(matriz,letras[1])
            
            if indicesLetra1[0] != indicesLetra2[0] and indicesLetra1[1] != indicesLetra2[1]:
                textoFinal += matriz[indicesLetra1[0]][indicesLetra2[1]]
                textoFinal += matriz[indicesLetra2[0]][indicesLetra1[1]]
            elif indicesLetra1[0] == indicesLetra2[0] and indicesLetra1[1] != indicesLetra2[1]:
                if indicesLetra1[1] + 1 > 4:
                    textoFinal += matriz[indicesLetra1[0] - 1][0]
                else:
                    textoFinal += matriz[indicesLetra1[0]][indicesLetra1[1] - 1]
                if indicesLetra2[1] + 1 > 4:
                    textoFinal += matriz[indicesLetra2[0] - 1][0]
                else:
                    textoFinal += matriz[indicesLetra2[0]][indicesLetra2[1] - 1]
            elif indicesLetra1[0] != indicesLetra2[0] and indicesLetra1[1] == indicesLetra2[1]:
                if indicesLetra1[0] + 1 > 5:
                    textoFinal += matriz[0][indicesLetra1[1] - 1]
                else:
                    textoFinal += matriz[indicesLetra1[0] - 1][indicesLetra1[1]]
                if indicesLetra2[0] + 1 > 5:
                    textoFinal += matriz[0][indicesLetra2[1] - 1]
                else:
                    textoFinal += matriz[indicesLetra2[0] - 1][indicesLetra2[1]]
        textoFinal = ''.join(textoFinal)
        
        return textoFinal        
    else:
        return "Deben ser strings"


def indicesMatriz(matriz,letra):
    indices = []
    for fila in matriz:
        if  letra in fila:
            indices.append(matriz.index(fila))
            indices.append(fila.index(letra))
    
    return indices

#----------------------------------------------------------------------------#



