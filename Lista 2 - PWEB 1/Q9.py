numeros = input("Digite uma lista de números separados por espaço: ").split()

soma = 0
for num in numeros:
    soma += int(num)

media = soma / len(numeros)

print("A média dos números é:", media)