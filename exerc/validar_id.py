import requests
import json
import re
from datetime import datetime, timedelta

ID_A_VALIDAR = 8346

data_fim = datetime.now()
data_inicio = data_fim - timedelta(days=90)
timestamp_inicio = int(data_inicio.timestamp())
timestamp_fim = int(data_fim.timestamp())

url_template = "https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start={}&end={}&_=1761849065862"

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://trainingserver.atec.pt/TrainingServer/GestaoFormacao/Horarios/UserCurrentSchedule.aspx',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'ASP.NET_SessionId=l2vz1qgejcb2wr4ue1vc4lso; .EVisionPortalASPXAUTH=57C7CBEA467FE5127079D15B8043EB175CF8E939E9AE37D7BE8AD1D129DFE4876659DEDC9744C1767180803394D7C4309ABFC5E0AFF8939852F478A1F58DF706FFA926F9BB5CFDDDF2B76A0C75EBFD751BAFF7F509DD7E7C45720E733458820ECE52D6A364D9EB8FE13E142E292AE4BD5T3B9C2BA37C4B2D7B62224732F234936131B72BC0E8FFACAD1AEE1F68FF6560; portalroles=CC0F31B99B7C0760D1D4553B3F489571623B6B752305DFA21CEA04B84AA982E0F33B31D25384DD61A48EDCAEC5C1FA123A0B216FCB3175392A8BC491D42ADEF3EE22A0AB461894B63B9AA5B75E6FA3835A51132EBE59A4D6F6B7298922F5347F66E44C7237F997C4109BBEB24C3DBCFB5112E18A2A8A69FEB4EEE9EDFC7B2D692240C0828BE546C8D784DEC42E0810D6B29D29CBCAA00B1A346CB35780E7981C'
}

regex_formador = re.compile(r"Formador:</u></b>\s*(.*?)\s*<br/>")

print(f"A validar o ID: {ID_A_VALIDAR}")
print(f"Período de pesquisa: de {data_inicio.strftime('%Y-%m-%d')} a {data_fim.strftime('%Y-%m-%d')}")


url_final = url_template.format(ID_A_VALIDAR, timestamp_inicio, timestamp_fim)
response = requests.get(url_final, headers=headers, timeout=10)
response.raise_for_status()

if response.text:
    eventos = response.json()
    if not eventos:
        print(f"\nRESULTADO: O ID {ID_A_VALIDAR} é VÁLIDO, mas não tem eventos de formação registados nos últimos 90 dias.")
    else:
        formadores_encontrados = set()
        for evento in eventos:
            descricao = evento.get('description', '')
            if "Sessão como Formador" in descricao:
                match = regex_formador.search(descricao)
                if match:
                    nome_extraido = match.group(1).strip()
                    if nome_extraido:
                        formadores_encontrados.add(nome_extraido)

        print("\n--- ANÁLISE DO ID ---")
        if not formadores_encontrados:
            print(f"O ID {ID_A_VALIDAR} não tem sessões 'como Formador' nos últimos 90 dias. Pode ser um ID de aluno ou inativo.")
        elif len(formadores_encontrados) == 1:
            nome_unico = list(formadores_encontrados)[0]
            print(f"RESULTADO: O ID {ID_A_VALIDAR} parece ser um formador VÁLIDO.")
            print(f"Nome associado encontrado: '{nome_unico}'")
        else:
            print(f"RESULTADO: O ID {ID_A_VALIDAR} parece ser um ID de ALUNO ou partilhado.")
            print(f"Foram encontrados múltiplos formadores associados: {formadores_encontrados}")
else:
    print(f"\nRESULTADO: O ID {ID_A_VALIDAR} é VÁLIDO, mas não tem quaisquer eventos registados nos últimos 90 dias.")
