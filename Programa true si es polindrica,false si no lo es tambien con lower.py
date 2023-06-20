# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 19:21:09 2023

@author: Alumno
"""

frase = input("Ingrese una frase: ")


frase = frase.replace(" ", "").lower()


es_palindromo = frase == frase[::-1]

print(es_palindromo)