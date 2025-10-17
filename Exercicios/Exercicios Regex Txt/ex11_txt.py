import re

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

nif_valido=re.findall(r"NIF:\s*([123568]\d{8})\b", ler_dados)

print(nif_valido)