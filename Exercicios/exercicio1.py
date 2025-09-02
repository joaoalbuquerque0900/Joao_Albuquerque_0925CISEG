nome=0
listanomes=[]

nome=input("Escreve um nome: ")

for char in nome:

    if not (ord(char)==32 or 65<=ord(char)<=90 or 97<=ord(char)<=122): #verificar se so tem maiusculas, minusculas e espaços
        print("\nnome invalido: caracteres nao reconhecidos")
        exit()
        


if '  ' in nome: #verificar se tem mais do que um espaço
    print("\nNome invalido: espacos a mais entre os nomes")
    exit()

if nome.count(' ')==0: #verificar se tem algum espaço
    print("\nnome invalido: falta espaco entre os nomes")
    exit()

nomes_separados=nome.split() #isolar os nomes

for nome_sep in nomes_separados: #verificar se em cada nome a primeira letra é maiscula e as restantes minusculas

    primeira_letra=nome_sep[0]
    
    if not (65<=ord(primeira_letra)<=90):
        print("\nNome invalido: a primeira letra de cada nome tem de ser maiscula")
        exit()

    for letra in nome_sep[1:]:

        if not (97<=ord(letra)<=122):
            print("\nnome invalido: apenas a primeira letra pode ser maiscula")
            exit()
    
print("\nNome valido") #caso todos os criterios sejam verificados, dizer que o nome e valido e dar append a lista de nomes
listanomes.append(nome)