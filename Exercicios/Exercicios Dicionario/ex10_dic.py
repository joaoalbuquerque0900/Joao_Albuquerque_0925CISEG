frase=input("Escreva uma frase: ")

lista_palavras=frase.split()

contador_palavras={}
contador=0
i=0

for palavra in lista_palavras:

    contador=0

    for i in range(len(lista_palavras)):

        if i in contador_palavras:

            continue

        if palavra==lista_palavras[i]:

            contador+=1

            contador_palavras[palavra]=contador

        else:
            continue

print(contador_palavras)

