nomes=[
    "Pedro Pereira",
    "Ana Clara",
    "Ana Beatriz",
    "Carlos Silva",
    "Beatriz Sousa",
    "Ana Paula",
    "Pedro Andrade"
    ]

i=0
j=0
nome=str

nomes_isolados=[]
nomes_ordenados=[]

nomes_ordenados=sorted(nomes)

for i in range(len(nomes_ordenados)):

    nome=nomes_ordenados[i]

    nomes_isolados.append(nome.split())


i=0

for i in range(len(nomes_isolados)):

    if i!=len(nomes_isolados)-1:

        if ord(nomes_isolados[i][1][0])>ord(nomes_isolados[i+1][1][0]):

            temporario=nomes_isolados[i]
            del nomes_isolados[i]
            nomes_isolados.insert(i+1, temporario)

        else:
            if ord(nomes_isolados[i][0][0])>ord(nomes_isolados[i+1][0][0]):

                temporario=nomes_isolados[i]  
                del nomes_isolados[i]
                nomes_isolados.insert(i+1,temporario)
    else:
        break

nomes_ordenados=nomes_isolados

print(nomes_ordenados)
        