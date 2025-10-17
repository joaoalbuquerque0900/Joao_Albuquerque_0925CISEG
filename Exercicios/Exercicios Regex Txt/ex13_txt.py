import re
from datetime import datetime

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

registos_completos = re.findall(r"Nome:.*", ler_dados)

padrao_data = re.compile(r"Data:\s*(\d{2}[/.-]\d{2}[/.-]\d{4})")


data_limite = datetime(2025, 1, 1)
registos_validos = []

for registo in registos_completos:
 
    correspondencia_data = padrao_data.search(registo)

    if correspondencia_data:
  
        data_str = correspondencia_data.group(1)
        data_objeto = datetime.strptime(data_str.replace('.', '/').replace('-', '/'), "%d/%m/%Y")

        if data_objeto < data_limite:

            registos_validos.append(registo)

if registos_validos:
    print("Foram encontrados os seguintes registos com data anterior a 2025:")
    for r in registos_validos:
        print(r)
else:
    print("Nenhum registo com data anterior a 2025 foi encontrado.")