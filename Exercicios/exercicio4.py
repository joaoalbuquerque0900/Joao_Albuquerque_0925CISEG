import os
import time

lista_frase=[]

def inverter_string(frase):

    global lista_frase

    frase_upper = frase.upper()
    frase_upper.replace(" ","")

    lista_frase=list(frase_upper)

    n = len(lista_frase)

    while n>1:
      
        troca=False

        i=0

        for i in range(n-1):
                
            if ord(lista_frase[i])<ord(lista_frase[i+1]):

                lista_frase[i], lista_frase[i+1]=lista_frase[i+1], lista_frase[i]
                troca=True
        
        if not troca:
            break

        n-=1
 
frase_input=input("Introduza uma frase: ")

inverter_string(frase_input)

i=0

for i in range(len(lista_frase)):

    print(lista_frase[i], end="")

            

