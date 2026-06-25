notas = []

print("Digite as notas (digite 'fim' para encerrar):")

while True:
    entrada = input("Nota: ")

    if entrada.lower() == 'fim':
        break

    nota = float(entrada)
    notas.append(nota)

if len(notas) == 0:
    print("Nenhuma nota foi digitada.")
else:
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    print(f"Média: {media:.2f}")
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
