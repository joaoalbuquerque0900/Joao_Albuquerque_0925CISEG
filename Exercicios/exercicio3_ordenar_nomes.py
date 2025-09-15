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

trocou=bool

nomes_ordenados=sorted(nomes)

for i in range(len(nomes_ordenados)):

    nome=nomes_ordenados[i]

    nomes_isolados.append(nome.split())


i=0

while True:

    trocou=False

    for i in range(len(nomes_isolados)):

        if i!=len(nomes_isolados)-1:

            if ord(nomes_isolados[i][0][0])>ord(nomes_isolados[i+1][0][0]):

                nomes_isolados[i], nomes_isolados[i+1] = nomes_isolados[i+1], nomes_isolados[i]
                trocou=True

            elif ord(nomes_isolados[i][0][0])==ord(nomes_isolados[i+1][0][0]):
                
                if ord(nomes_isolados[i][1][0])>ord(nomes_isolados[i+1][1][0]):

                    nomes_isolados[i], nomes_isolados[i+1] = nomes_isolados[i+1], nomes_isolados[i]
                    trocou=True

    if not trocou:
        break

nomes_ordenados=nomes_isolados

print(nomes_ordenados)
        