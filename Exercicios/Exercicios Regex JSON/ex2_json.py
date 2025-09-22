import json
import re

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.json","r") as ficheiro:

    dados=json.load(ficheiro)


padrao_email=r"^[\w\.-]+@[\w\.-]+\.\w+$"

for pessoa in dados:

    email=pessoa.get("email","")

    if re.match(padrao_email, email):

        print(f"Email valido: {email}")
    else:
        print(f"Email invalido {email}")