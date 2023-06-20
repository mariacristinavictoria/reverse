# -*- coding: utf-8 -*-


cadena1 = ("hola")
cadena2 = ("hola  mundo  feliz")


if cadena1 in cadena2:
    print("la cadena 1 esta presente en la cadena 2")

cadena2 = cadena2.replace("  ", " ")
print(cadena2)