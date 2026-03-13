number = 29
for i in range(1, number):
    if number % i == 0:
        print("O número", number, "não é primo!")
        break

    else:

        print("O número", number, "é primo")