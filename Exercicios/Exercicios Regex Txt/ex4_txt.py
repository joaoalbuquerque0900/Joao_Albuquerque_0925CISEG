import re

nomes=[]

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.txt", "r") as dados:

    ler_dados=dados.read()

padrao_nome=r"Nome:\s*([^,]+)"

nomes=re.findall(padrao_nome, ler_dados)

print(nomes)