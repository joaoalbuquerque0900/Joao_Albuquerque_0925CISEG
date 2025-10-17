import re

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

emails_pt=re.findall(r"Email:\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.pt)", ler_dados)

print(emails_pt)