notas = { 

    'João': [7, 8, 9], 

    'Maria': [10, 9, 8], 

    'Ana': [6, 7, 8] 

} 

medias={}

acumulador_notas=0
contador_notas=0

for chave in notas:

    acumulador_notas=0
    contador_notas=0

    for i in range(len(notas[chave])):

        contador_notas+=1
        acumulador_notas+=notas[chave][i]

    medias[chave]=acumulador_notas/contador_notas


for aluno in medias:
    
    print(f"{aluno}: {medias[aluno]}")    