def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Calculadora em Python")
print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

op = input("Digite a opção (1/2/3/4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if op == '1':
    print("Resultado:", somar(num1, num2))
elif op == '2':
    print("Resultado:", subtrair(num1, num2))
elif op == '3':
    print("Resultado:", multiplicar(num1, num2))
elif op == '4':
    print("Resultado:", dividir(num1, num2))
else:
    print("Opção inválida.")
