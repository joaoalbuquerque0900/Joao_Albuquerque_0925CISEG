import json


with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.json","r") as ficheiro:

    dados=json.load(ficheiro)

for pessoa in dados:

    nif=pessoa.get("nif","")

    if nif[0]=="1" or nif[0]=="2" or nif[0]=="3" or nif[0]=="5" or nif[0]=="6" or nif[0]=="8":

        contador=0

        for char in nif:

            contador+=1

        if contador==9:
            print(F"{nif}: NIF valido")
        
        else:
            print(F"{nif}: NIF invalido")
    
    else:

        print(F"{nif}: NIF invalido")