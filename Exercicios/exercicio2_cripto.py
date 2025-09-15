import os
import time

mensagem=""
chave=""
palpite=""

lista_mensagem=[]
lista_chave=[]
lista_palpite=[]
lista_subtracao=[]
lista_final=[]

valor_chave=0
contador_tentativas=0

i=0
op_menu=0


def criptografar():

    global lista_mensagem
    global lista_final
    global lista_chave
    global lista_subtracao
    global i
    global valor_chave
    global mensagem
    global chave

    valor_chave=0
    lista_mensagem=[]
    lista_chave=[]
    lista_subtracao=[]
    lista_final=[]

    while True:

        os.system("cls")

        mensagem=input("Defina a mensagem que pretende criptografar: ")

        if mensagem=="":
            print("\nA mensagem nao pode estar vazia, tente outra vez.")
            time.sleep(2)
            continue
        else:
            break

    while True:

        os.system("cls")

        chave=input("Defina uma chave: ")

        if chave=="":

            print("\nA chave nao pode estar vazia, tente outra vez.")
            time.sleep(2)
            continue

        else:
            break


    for char in chave:

        lista_chave.append(ord(char))
        valor_chave+=ord(char)
    

    for char in mensagem:

        lista_mensagem.append(ord(char)+valor_chave)


    i=0
    lista_final=list(lista_mensagem)

    for i in range(len(lista_mensagem)):

        if lista_mensagem[i]<133:

            lista_final.insert(i, chr(lista_mensagem[i]-30))
            del lista_final[i+1]
            lista_subtracao.append(30)
        
        else:
            
            lista_subtracao.append(0)

            while lista_final[i]>126:

                lista_final[i]-=100
                lista_subtracao[i]+=100
            
            lista_final.insert(i,chr(lista_final[i]))
            del lista_final[i+1]
 

    
def descriptografar():

    global lista_chave
    global lista_mensagem
    global lista_palpite
    global i
    global palpite
    global mensagem
    global contador_tentativas
    global chave

    contador_tentativas=0

    while True:

        os.system('cls')

        
        if mensagem=="":

            print("\nAinda nao foi definida uma mensagem")
            time.sleep(2)
            break
        else:
            pass

        palpite=input("Digite a chave: ")

        if palpite=="":

            print("\nEste campo nao pode estar vazio, tente outra vez")
            time.sleep(2)
            continue
        else:
            pass

        lista_palpite=[]

        for char in palpite:

            lista_palpite.append(ord(char))

    
        if lista_palpite==lista_chave:

            os.system('cls')
            
            print(f"Chave correta.\n\nMensagem: {mensagem}")
            time.sleep(2)
            break

        else:
                
            if contador_tentativas<3:

                contador_tentativas+=1

                print(f"\nChave errada, sobram-lhe {3 - contador_tentativas}")
                time.sleep(2)
                continue
            else:

                print("\nEsgotou as tentativas.")
                break

def listar():

    global lista_final
    global i

    i=0

    while True:

        if mensagem=="":

            print("\nAinda nao foi definida uma mensagem")
            time.sleep(2)
            break
        else:
            pass

        os.system('cls')

        for i in range(len(lista_final)):

            print(lista_final[i], end="", flush=True)
            time.sleep(0.1)

        time.sleep(5)
        os.system('cls')
        break

while True:

    os.system('cls')

    print("1 - Criptografar mensagem")
    print("\n2 - Descriptografar")
    print("\n3 - Listar mensagem criptografada")
    print("\n4 - Sair do programa")

    try:

        op_menu=int(input("\n\nEscolha uma opcao: "))

    except:

        print("\nValor invalido, tente outra vez")
        time.sleep(2)
        continue

    match(op_menu):

        case 1:

            criptografar()
            continue

        case 2:

            descriptografar()
            continue

        case 3:

            listar()
            continue

        case 4:

            print("\nObrigado")
            time.sleep(2)
            break

        case _:

            print("\nEssa opcao nao consta no menu, tente outra vez.")
            time.sleep(2)
            continue