# 1 - Ler um valor inteiro 
# (aceitar somente valores entre 1 e 10) e 
# escrever a tabuada de 1 a 10 do valor lido.

interr = int(input("Apresente o valor: "))

if interr < 1 or interr > 10:
    print("Reenvie o valor")

else:
    for i in range(1, 11, 1):
        print(interr," * ", i , " = ", i * interr)
