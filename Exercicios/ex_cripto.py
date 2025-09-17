#FALTA O ULTIMO PONTO DA ROTACAO, E ISTO TA COM UMA FORMATACAO ESTRANHA QUANDO DOU PRINT NA MENSAGEM ENCRIPTADA
#NAO SEI SE A FUNCAO PARA DESENCRIPTAR NAO É NECESSARIO PEDIR AO USER A CHAVE PARA DESBLOQUEAR A MENSAGEM

import time
import os

def criptografar(mensagem:str, chave: str):

    global lista_chave
    global lista_mensagem
    global char
    global i
    global valor_chave
    global valor_mensagem

    for char in chave:

        lista_chave.append(ord(char))
    
    i=0
    valor_chave=0

    for i in range(len(lista_chave)):

        valor_chave+=lista_chave[i]

    valor_mensagem=0

    for char in mensagem:

        lista_mensagem.append(ord(char)+valor_chave)

    print("Mensagem encriptada: ")
    
    i=0

    for i in range(len(lista_mensagem)):

        print(lista_mensagem[i],end="")  
        

    time.sleep(3.5)
    os.system('cls')  


def descriptografar(codigos: list[int], chave: str):

    global lista_mensagem
    global valor_chave
    global i 
    global mensagem_decript

    i=0

    for i in range(len(lista_mensagem)):

        mensagem_decript.append(lista_mensagem[i]-valor_chave)
    
    i=0

    for i in range(len(mensagem_decript)):

        print(chr(mensagem_decript[i]),end="")

    time.sleep(3.5)
    os.system('cls')  

def listar():

    global lista_mensagem
    global i

    i=0

    for i in range(len(lista_mensagem)):
        
        print(f"\n{lista_mensagem[i]}")
        time.sleep(0.5)

    time.sleep(3.5)
    os.system('cls')  

mensagem=str
chave=str
mensagem_decript=[]
char=chr
i=0
valor_chave=0
valor_mensagem=0
lista_chave=[]
lista_mensagem=[]


while True:

    os.system('cls')

    print("1 - Criptografar")
    print("\n2 - Descriptografar")
    print("\n3 - Listar mensagem encriptada")
    print("\n4 - Sair do programa")

    try:
        op_menu=int(input("\n\nEscolha uma opcao: "))

    except:
        print("\n\nValor invalido, tente outra vez")
        time.sleep(2)
        continue

    match(op_menu):

        case 1:

            os.system('cls')
            
            mensagem=input("Defina uma mensagem: ")
            os.system('cls')

            while True:

                chave=input("Defina uma chave: ")

                if chave=="":
                    print("\nA chave nao pode estar vazia. Tente outra vez")
                    time.sleep(2)
                    os.system('cls')
                    continue
                else:
                    break

            criptografar(mensagem, chave)
        
        case 2:

            os.system('cls')

            if chave=="":
                print("Ainda nao foi definida mensagem nem chave")
                time.sleep(2)
                os.system('cls')
                continue
            else:
                pass

            descriptografar(lista_mensagem, chave)
            continue

        case 3:

            os.system('cls')

            if len(lista_mensagem)==0:

                print("Ainda nao foi definida uma mensagem para listar")
                time.sleep(2)
                continue
            else:
                pass

            listar()
            continue

        case 4:

            os.system('cls')
            print("Obrigado")
            time.sleep(2)
            break

        case _:

            os.system('cls')
            print("Essa opcao nao consta no menu, tente outra vez.")
            time.sleep(2)
            continue
                
                

