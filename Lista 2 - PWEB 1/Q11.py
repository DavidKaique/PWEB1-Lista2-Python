numeros = input("Digite uma lista de números separados por espaço: ").split()

for x in numeros:
    if int(x) % 2 != 0:
        print("Os numeros impares inseridos na lista são:", x)