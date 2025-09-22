import json


with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.json","r") as ficheiro:

    dados=json.load(ficheiro)


with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados_texto.txt","w") as ficheiro_txt:

    for pessoa in dados:

        nome=pessoa.get("nome", "")
        email=pessoa.get("email", "")

        ficheiro_txt.write(f"Nome: {nome} -- Email: {email}\n")

print("\nFicheiro de texto criado com sucesso: dados_texto.txt")
