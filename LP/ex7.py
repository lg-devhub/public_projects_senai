# 2 - Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
# Enquanto o número digitado não for igual a um número secreto definido pelo programa,
# o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
# o programa deve imprimir "Parabéns, você acertou!".
# Use a biblioteca abaixo para números aleatórios:
# import random
# numero_secreto = random.randint(1, 100)
import random
number = random.randint(1, 100)

descubra = int(input("Apresente seu valor:"))

if descubra == number:
    print("Parabéns, você acertou!")
elif descubra != number:
    print("Faça novamente")