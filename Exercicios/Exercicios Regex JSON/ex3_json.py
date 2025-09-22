import json
from urllib.parse import urlparse

with open("C:\DEV\Joao_Albuquerque_0925CISEG\dados.json","r") as ficheiro:

    dados=json.load(ficheiro)


for pessoa in dados:

    site = pessoa.get("site", "")
    dominio_site=urlparse(site).netloc
    print(dominio_site)