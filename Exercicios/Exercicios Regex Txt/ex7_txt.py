import re

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

nif=re.findall(r"NIF:\s*(\d{9})\b",ler_dados)

print(nif)