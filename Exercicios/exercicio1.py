nome=0
listanomes=[]

nome=input("Escreve um nome: ")

for char in nome:

    if not (ord(char)==32 or 65<=ord(char)<=90 or 97<=ord(char)<=122):
        print("\nnome invalido: caracteres nao reconhecidos")
        exit()
        


if '  ' in nome:
    print("\nNome invalido: espacos a mais entre os nomes")
    exit()

if nome.count(' ')==0:
    print("\nnome invalido: falta espaco entre os nomes")
    exit()

nomes_separados=nome.split()

for nome_sep in nomes_separados:

    primeira_letra=nome_sep[0]
    
    if not (65<=ord(primeira_letra)<=90):
        print("\nNome invalido: a primeira letra de cada nome tem de ser maiscula")
        exit()

    for letra in nome_sep[1:]:

        if not (97<=ord(letra)<=122):
            print("\nnome invalido: apenas a primeira letra pode ser maiscula")
            exit()
    
print("\nNome valido")
listanomes.append(nome)