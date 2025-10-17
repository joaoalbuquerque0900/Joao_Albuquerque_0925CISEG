import re

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

datas=re.findall(r"Data:\s*(\d{2}[/.-]\d{2}[/.-]\d{4})", ler_dados)

print(datas)