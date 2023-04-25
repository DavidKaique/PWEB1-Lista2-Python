numeros = input("Digite uma lista de números separados por espaço: ").split()

soma = 0
for x in numeros:
    soma += int(x)

print("A soma dos números é:", soma)