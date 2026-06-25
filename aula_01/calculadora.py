print(" --- Calculadora ---")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")


# print(a,b)
# print(op)

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
     if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
     else:
        resultado = num1 / num2
else:
    print("Operação inválida.")

print(f"O resultado é: {resultado}")
        