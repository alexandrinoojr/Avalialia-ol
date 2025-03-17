# input para inverter string
texto = input("Digite uma string para inverter: ")

texto_invertido = ""

# Percorre a string de trás para frente e atribui a variavel text_invertido
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

print(f"String invertida: {texto_invertido}")
