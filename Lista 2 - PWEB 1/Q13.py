numeros = input("Digite a lista de números separados por espaço: ").split()
numeros = list(map(int, numeros))

numeros_ordenados = sorted(numeros)

print("A lista em ordem crescente é:", numeros_ordenados)