numeros = input("Digite a lista de números separados por espaço: ").split()
numeros = list(map(int, numeros))

numeros_ordenados = sorted(numeros, reverse=True)

print("A lista em ordem decrescente é:", numeros_ordenados)