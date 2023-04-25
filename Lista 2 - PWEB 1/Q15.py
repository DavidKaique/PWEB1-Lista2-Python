numeros = input("Digite uma lista de números separados por espaço: ").split()

x = input("Digite um número para verificar se está na lista: ")

if x in numeros:
    print("O número", x, "está na lista!")
else:
    print("O número", x, "não está na lista.")