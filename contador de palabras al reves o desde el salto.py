# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:40:59 2023

@author: Alumno
"""

def obtener_palabras_de_cinco_caracteres(lista):
    palabras_de_cinco = []
    for palabra in lista:
        if len(palabra) == 5:
            palabras_de_cinco.append(palabra)
    return palabras_de_cinco

lista_ejemplo = ["aa", "b", "camiseta", "cacao", "platano", "cereza", "cacahuete","manos","caras"]
resultado = obtener_palabras_de_cinco_caracteres(lista_ejemplo)
print("Las palabras de cinco caracteres son:", resultado)