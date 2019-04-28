def cesarCod(texto,desplazamiento):
    abecedario = "abcdefghijklmnñopqrstuvwxyz" 
    contador = 0
    if isinstance (texto, str) and (desplazamiento, int):
        textocod = ""
        for letra in texto:
            if letra == " ":
                textocod += " "
            else:
                ces = abecedario.index(texto[letra] + desplazamiento)
                mod = int(ces) % 26
                textocod = textocod + str(abecedario.index[mod])
        return textocod
    else:
        return "Texto debe ser un string y desplazamiento un numero entero"


def cesarDec(texto,desplazamiento):
    abecedario = "abcdefghijklmnñopqrstuvwxyz" + "abc"





# -*- coding: utf-8 -*- 

class Caesar(): 
    def __init__(self): 
        # Lista de caracteres a usar. 
        self.caract = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789" 

    def cifrar(self, cadena, clv): 
        ''' 
        Función que cifrará nuestro mensaje, a partir de la cadena y clave proporcionada. 
        ''' 
        resultado = "" 
        for letra in cadena: 
            if letra == " ": 
                resultado += " " 
            else: 
                op = self.caract.find(letra) + clv 
                modulada = int(op) % 37 
                resultado = resultado + str(self.caract[modulada]) 

        return(resultado) 

    def descifrar(self, cadena, clv): 
        ''' 
        Función que descifrará nuestro mensaje cifrado, a partir de una clave y cadena proporcionada.
        ''' 
        resultado = "" 
        for letra in cadena: 
            if letra == "": 
                resultado += "" 
            else: 
                op = self.caract.find(letra) - clv 
                modulada = int(op) % 37 
                resultado = resultado + str(self.caract[modulada]) 

        return(resultado) 

op = str(input("Deseas cifrar o descifrar? ")).lower() 
if op == "cifrar": 
    cadena = str(input("Cadena a cifrar: ")).upper() 
    clv = int(input("Clave a usar: ")) 
    r = Caesar() 
    a = r.cifrar(cadena, clv) 
    print(a) 
elif op == "descifrar": 
    cadena = str(input("Cadena a descifrar: ")).upper() 
    clv = int(input("Clave a usar: ")) 
    r = Caesar() 
    a = r.descifrar(cadena, clv) 
    print(a) 
