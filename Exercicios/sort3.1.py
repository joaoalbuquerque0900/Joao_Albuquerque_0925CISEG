listaNome=["Dario Quental","Dario Almeida","Bruno Carvalho"]
# index         0                1                 2
#length 3
 
i=0 # Variavel que controla a primeira posiçao ( nome )
it=0 # Variavel que controla a segunda posiçao ( letra do nome )
controloTroca=-1 # guarda a posiçao da 1 dimensao(nome inteiro) que existiu uma troca
il=1 # Variavel que controla as rotações a lista inteira
 
while il<len(listaNome):       # Loop controla as voltas a lista

    i=0                # reposiçao do index da lista 1 dimensão ( Nome )
    print("IL - ",il)
    
    while i< len(listaNome):  # Loop controla a posiçao do nome

        print("\n\n","index 1 pos - ",i,"\n\n")

        if i<=len(listaNome)-2:

            it=0  # reposiçao do index da lista 2 dimensão ( Letras )
            controloTroca=-1 # reposiçao da variavel troca // tambem seria possivel usar um break

            while it<len(listaNome[i]) and it< len(listaNome[i+1]): # Loop controla as letras no nome

                print("index 2 pos - ",it," Valor Controla troca ", controloTroca)

                if it == 0 and listaNome[i][0] == listaNome[i+1][0]:

                    if ord(listaNome[i].split()[1][0]) > ord(listaNome[i+1].split()[1][0]):

                        listaNome[i], listaNome[i+1] = listaNome[i+1], listaNome[i] 
                        controloTroca = i
                        break

                    break

                if ord(listaNome[i][it]) > ord(listaNome[i+1][it]) and  controloTroca != i :

                    print("If da troca posicao do i", i ," posiçao do  it", it )
                    print (listaNome[i][it] , "   -   " , listaNome[i+1][it] )
                    controloTroca=i # controlar index da primeira dimençao ( quando acontece troca de nome ja nao é trocado nenhum nome)
                    listaNome[i], listaNome[i+1] = listaNome[i+1], listaNome[i]  
                    print(listaNome)    
                    break

                it+=1                        
        i+=1
    il+=1
 
print(listaNome)