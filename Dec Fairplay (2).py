##Cifrado FairPlay ##
## Utliza una palabra clave ##
## Esta palabra entra en las listas y se borran los caracteres iguales##

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
