#!/usr/bin/python
Abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ##Abecedario Utilizado
Mensaje = input("Ingresa el Mensaje a Cifrar:  ").upper() ##Pedimos el mensaje a cifrar
Clave = input("Ingresa la Clave:  ").upper() ##Pedimos la clave a utilizar
Final = "" ##Resultado final
I = 0  ##posicion actual en el mensaje de la letra que se esta cifrando
 
for x in Mensaje: ##recorremos el mensaje a cifrar
 
    if x == " ":
        Final += " "
    else: 
        Mod_cl=I%len(Clave) ##segun la letra en la que estemos, sabremos que letra de la clave se le fue asignada
        Asignada=Clave[Mod_cl] ##obtenemos la letra clave asignada
        Sumando=Abecedario.find(x)+Abecedario.find(Asignada) ##sumamos la letra del mensaje y la letra clave asignada a la misma
        Modulo=(Sumando%26) ##obtenido el resultado de la suma, lo modulamos con la longitud del abecedario utilizado
        Final=Final+Abecedario[Modulo] ##Sumamos la letra cifrada, al conjunto de respuesta
        I=I+1 ##aumentamos una posicion, para cifrar la siguiente letra del mensaje
         
print (Final) ##revelamos el resultado final
