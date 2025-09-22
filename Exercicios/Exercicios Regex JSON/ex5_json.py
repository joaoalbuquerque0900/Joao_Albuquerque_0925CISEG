import json
import re

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.json","r") as ficheiro:

    dados=json.load(ficheiro)

padrao_email=r"^[\w\.-]+@[\w\.-]+\.\w+$"
dados_validos=[]
contador_telemovel=0

for pessoa in dados:

    email=pessoa.get("email","")

    if re.match(padrao_email, email):

        pass

    else:

        continue

    nif=pessoa.get("nif","")

    if nif[0]=="1" or nif[0]=="2" or nif[0]=="3" or nif[0]=="5" or nif[0]=="6" or nif[0]=="8":

        contador=0

        for char in nif:

            contador+=1

        if contador==9:
            
            pass
        
        else:
            continue
    
    else:

        continue

    telemovel=pessoa.get("telemovel","")

    contador_telemovel=0

    for char in telemovel:

        if char.isdigit():

            contador_telemovel+=1

        else:
            continue
    
    if contador_telemovel==9:

        dados_validos.append(pessoa)

    else:

        continue

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados_validos.json","w") as ficheiro_novo:

    json.dump(dados_validos, ficheiro_novo, indent=4)

print("Ficheiro criado com sucesso")