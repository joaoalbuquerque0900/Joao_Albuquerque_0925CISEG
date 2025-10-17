import re

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

codigo_postal=re.findall(r"Código Postal:\s*(\d{4}-\d{3})",ler_dados)

print(codigo_postal)