# dados de faturamento 
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

# valida se o faturamento total é maior que zero 
if faturamento_total > 0:
    print("Percentual de representação por estado:\n")

    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")
else:
    print(" Não existe valor para ser calculado.")
