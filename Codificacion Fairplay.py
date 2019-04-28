##Cifrado FairPlay ##
## Utliza una palabra clave ##
## Esta palabra entra en las listas y se borran los caracteres iguales##

abecedario = ['a','b','c','d','e','f','g','h','i','j','k',\
             'l','m','n','ñ','o','p','q','r','s','t','u',\
             'v','w','x','y','z']

def playfairCod (palabra, texto):
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
        listexto = []
        lispalabra = list(texto)
        for i in texto:
            if i in abecedario:
                if lispalabra [-1] == i:
                    lispalabra.append("1")
                    lispalabra.append(i)
                else:
                    lispalabra.append(i)
        k = len(texto)//2
        pp = 0
        op = 1
        nuevalista = []
        while k > 0:
            while op < len(lispalabra)//2:
                listak = lispalabra[pp] + lispalabra[pp+1]
                if lispalabra[pp] == lispalabra[pp+1]:
                    listak[1] = ['1']            
                nuevalista.append([listak])
                pp += 2
                op += 2
                k -= len(palabra)
        
        #return nuevalista
        return matriz
        return lispalabra



    else:
        return "Deben ser strings"


