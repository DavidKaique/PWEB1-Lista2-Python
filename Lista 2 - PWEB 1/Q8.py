numeros = input("Digite a lista de números separados por espaço: ").split()
numeros = list(map(int, numeros))  

maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)