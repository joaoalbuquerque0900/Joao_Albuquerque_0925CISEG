vendas={"Janeiro": 1000, "Feveiro": 1500, "Marco": 1200}
i=0
acumulador_vendas=0

for mes in vendas:

    acumulador_vendas+=vendas[mes]

print(f"Total Vendas: {acumulador_vendas}")