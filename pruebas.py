# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 00:33:40 2022

@author: espar
"""

numeros = [0,0,0,0]
    

frecuencia2 = 0
frecuencia = {}

for n in numeros:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1
        
print (numeros)
print ("Con frecuencia de: ", frecuencia)

if (frecuencia [n] == 4):
    print ("c termino")
else:
    print("no se termino")
    