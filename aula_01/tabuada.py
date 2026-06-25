numero = int(input("\nQual tabuada você deseja? "))
print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")
    