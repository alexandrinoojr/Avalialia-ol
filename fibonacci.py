#Resposta questão 02:
#função que sera chamada para validar a sequencia de fibonnaci
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False
#entrada de dados
num = int(input("Digite um número: "))

#validação da sequencia
if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")