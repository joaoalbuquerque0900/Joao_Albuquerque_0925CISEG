import re

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

nomes=re.findall(r"Nome:\s*([^,]+)", ler_dados)
emails=re.findall(r"Email:\s*([^,]+)", ler_dados)
telemoveis=re.findall(r"Telemóvel:\s*([^\n]+)", ler_dados)

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados_extraidos.txt", "w", encoding="utf-8") as dados:

    for nome, email, telemovel in zip(nomes, emails, telemoveis):

        dados.write(f"{nome} | {email} | {telemovel}\n")

print("Sucesso")