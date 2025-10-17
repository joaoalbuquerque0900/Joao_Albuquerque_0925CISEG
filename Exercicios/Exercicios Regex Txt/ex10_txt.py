import re

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

dominios=re.findall(r"Site:\s*(?:https?://)?((?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})", ler_dados)

print(dominios)