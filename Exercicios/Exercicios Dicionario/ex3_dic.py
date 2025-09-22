produto={}

produto["nome"] = "Telemovel"
produto["preco"] = 1500
produto["stock"] = 30

print(f"Dicionario inicial: {produto}")

del produto["stock"]

print(f"Dicionario final: {produto}")