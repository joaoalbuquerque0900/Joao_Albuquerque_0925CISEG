import re

telemoveis=[]

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.txt", "r") as dados:

    ler_dados=dados.read()

padrao_telemovel=r"\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b"

telemoveis=re.findall(padrao_telemovel, ler_dados)

print(telemoveis)
