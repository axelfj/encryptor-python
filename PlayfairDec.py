
def playfairDecipher(texto, palabra):
    if isinstance(texto, str) and isinstance(palabra, str):
        abecedario = ['a', 'b','c','d' ,'e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
        matriz = [[], [], [], [], [],[]]
        abecedarioNuevo = list(palabra)
        k = 0
        for i in abecedario:
            if i not in abecedarioNuevo:
                abecedarioNuevo.append(i)        
        abecedarioNuevo.append('1')
        abecedarioNuevo.append('2')
        abecedarioNuevo.append('3')
        for i in matriz:
            for x in range(5):
                i.append(abecedarioNuevo[k])
                k += 1
        listaFrase = []
        listaPalabra = []
        for i in texto:
            if i in abecedario:
                if listaPalabra == []:
                    listaPalabra.append(i)
                elif listaPalabra[-1] == i:
                    listaPalabra.append('1')
                    listaPalabra.append(i)
    
                else:
                    listaPalabra.append(i)
            else:
                if len(listaPalabra)%2==1:
                    listaPalabra.append('1')
                listaFrase.append(listaPalabra)
                listaFrase.append(i)
                listaPalabra = []
        if listaPalabra!= []:
            if len(listaPalabra)%2==1:
                    listaPalabra.append('1')
            listaFrase.append(listaPalabra)
        for lista in listaFrase:
            if isinstance(lista, list):
                n = 0
                while n < len(lista):
                    lista[n], lista[n + 1] = letters(lista[n], lista[n + 1], matriz)
                    n += 2
        #str1 = "".join(listaFrase)
        return listaFrase

                    
def letters(a, b, matrix):
    i1,j1 = 0,0
    i2,jj2 = 0,0
    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            
            if matrix[i][j] == a:
                i1= i
                j1 = j
            if matrix[i][j] == b:
                i2 = i
                j2 = j
                
    if i1 != i2 and j1 != j2:
        a = matrix[i1][j2]
        b = matrix[i2][j1]
        return a,b 
    elif i1 == i2 and j1 != j2:
        a = matrix[i1][(j1 - 1) % 5]
        b = matrix[i2][(j2 - 1) % 5]
        return a,b 
    else:
        a = matrix[(i1 - 1) % 6][j1]
        b = matrix[(i2 - 1) % 6][j2]
        return a,b 
