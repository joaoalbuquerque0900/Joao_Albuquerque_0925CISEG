import re

emails=[]

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.txt", "r") as dados:

    ler_dados=dados.read()


emails=re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", ler_dados)

print(emails)