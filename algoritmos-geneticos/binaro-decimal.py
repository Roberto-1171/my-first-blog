import random



def conversion():
    print("--------------------------------------------------")
    poblacion = int(input("Ingrese el tamaño de la poblacion: "))
    ristra = int(input("Ingrese el tamaño de la Ristra: "))
    individuo = []
    print("--------------------------------------------------")
    for i in range (poblacion):
        binario = random.choices([0,1], k=ristra)
        individuo.append(binario)
        #print("numero de individuo}:","{",i,"}","=",individuo)
    for i in range (len(individuo)):
        numero = i + 1
        print(f"Numero de individuo[{numero}]: {individuo[i]}")
        
    for i in range (len(individuo)):
        numero = i + 1
        decimal = (str(binario), 2)
        print(f"Numero decimal[{numero}]: {decimal}" )


    """decimal = (int(str(binario), 2))
        print(decimal)"""
        
conversion()