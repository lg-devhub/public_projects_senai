

selec = input(str("Deseja par ou ímpar? par/impar"))

for i in range(1, 101):
    if selec == "par" and i % 2 == 0:
        print("O valor", i, "é par.")
    elif selec == "impar" and i % 2 != 0:
        print("O valor", i, "é impar")
    else:
        print("Entre com o valor correto!")