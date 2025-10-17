import re

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\registos.txt", "r", encoding="utf-8") as dados:

    ler_dados=dados.read()

padrao_completo = re.compile(
    r"Nome:\s*(?P<nome>[^|]+?)\s*\|\s*"          
    r"NIF:\s*(?P<nif>\d{9})\s*\|\s*"             
    r"Data:\s*(?P<data>\d{2}[/.-]\d{2}[/.-]\d{4})\s*\|\s*" 
    r"Código Postal:\s*(?P<cp>\d{4}-\d{3})\s*\|\s*"      
    r"Site:\s*(?:https?://)?(?P<site>\S+)"       
)

linhas_resumo = []

for correspondencia in padrao_completo.finditer(ler_dados):

    nome = correspondencia.group("nome").strip() 
    nif = correspondencia.group("nif")
    data = correspondencia.group("data")
    cp = correspondencia.group("cp")
    site = correspondencia.group("site")

    linha_formatada = f"{nome} | {nif} | {data} | {cp} | {site}"
    linhas_resumo.append(linha_formatada)

with open(r"C:\DEV\Joao_Albuquerque_0925CISEG\resumo.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(linhas_resumo))

print("Ficheiro 'resumo.txt' criado com sucesso!")
print(f"Foram processados e guardados {len(linhas_resumo)} registos.")