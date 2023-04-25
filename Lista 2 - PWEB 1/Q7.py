numero = int(input("Digite um número inteiro para a sequência de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci até", numero, ":")
print(a) 

while b <= numero:
    print(b)  
    a, b = b, a + b 