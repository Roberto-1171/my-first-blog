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


def Bindec (n):
    s=0
    i=0
    print("el binario", n)
    while (n>=1):
        d = n%10
        n = int(n/10)
        s = s+d*pow(2,i)
        i=i+1
    print("corresponde al numero",s)

numero = int(input("Ingrese el numero binario: ")) 
Bindec(numero)


#conversion()