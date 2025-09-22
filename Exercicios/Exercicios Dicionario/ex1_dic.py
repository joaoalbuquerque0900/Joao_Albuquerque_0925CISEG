import os
import time

aluno={"nome": "", "idade": 0, "curso": ""}
lista_alunos=[]
contador=0

op_menu=0

def inserir_aluno():

    global aluno
    global lista_alunos
    global contador

    while True:

        os.system('cls')


        nome=input("Nome do aluno: ")

        if nome=="":
            print("\nO nome nao pode estar vazio")
            time.sleep(2)
            os.system('cls')
            continue
        else:
            break
    
    while True:

        os.system('cls')

        try:
            idade=int(input("\nIdade do aluno: "))
            break
        except:
            print("\nValor invalido, tente outra vez")
            time.sleep(2)
            os.system('cls')
            continue
    
    while True:

        os.system('cls')

        curso=input("\nCurso do aluno: ")

        if curso=="":

            print("\nO campo do curso nao pode estar vazio, tente outra vez")
            time.sleep(2)
            os.system('cls')
            continue
        else:
            break
    
    aluno={"nome": nome, "idade": idade, "curso": curso}

    lista_alunos.append(aluno)
    contador+=1


def listar_alunos():

    global lista_alunos
    global contador

    while True:

        os.system('cls')

        if contador==0:

            print("Ainda nao foram registados alunos, tente outra vez mais apos registar")
            time.sleep(2)
            break
        else:
            pass

        i=0

        for i in range(len(lista_alunos)):

            print(f"\nNome: {lista_alunos[i]["nome"]}")
            print(f"\nIdade: {lista_alunos[i]["idade"]}")
            print(f"\nCurso: {lista_alunos[i]["curso"]}")
            print("\n--------")

            time.sleep(1)

        time.sleep(5)
        break

while True:

    os.system('cls')

    print("1 - Inserir aluno") 
    print("\n2 - Listar alunos")
    print("\n3 - Sair do programa")

    try:
        op_menu=int(input("\n\nEscolha uma opcao: "))
    except:
        print("\nValor invalido tente outra vez")
        time.sleep(2)
        continue

    match(op_menu):

        case 1:

            inserir_aluno()
            continue

        case 2:

            listar_alunos()
            continue

        case 3:

            print("\n\nObrigado")
            time.sleep(2)
            break

        case _:

            print("\nEssa opcao nao consta no menu, tente outra vez")
            time.sleep(2)
            continue

        

