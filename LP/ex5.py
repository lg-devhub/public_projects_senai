#0 - Peça para  o usuário entrar com dois valores (primeiro e último).
#Faça a contagem entre esses números.
#Caso o último for menor que  o primeiro faça a contagem decrescente.
#Caso o último número for maior que o primeiro faça a contagem crescente.

valor1 = int(input("Entre com o primeiro valor"))
valor2 = int(input("Entre com o segundo valor"))

if valor1 < valor2:
    for i in range(valor2, valor1, -1):
        print(i, end=" ")

elif valor2 < valor1:
    for i in range(valor2, valor1, 1):
        print(i, end=" ")