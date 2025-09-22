import time
import os

palavra=input("Escreva uma palavra: ")

lista_letras=[]
contador_letras={}
contador=0

for char in palavra:

    lista_letras.append(char)

for letra in lista_letras:

    contador=0
    i=0

    for i in range(len(lista_letras)):

        if i in contador_letras:

            continue

        if letra==lista_letras[i]:

            contador+=1

            contador_letras[letra]=contador

        else:
            continue

print(contador_letras)



        







