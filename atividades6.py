nomes = []

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")

nomes.append(nome1)
nomes.append(nome2)
nomes.append(nome3)

nomes.sort()

print("\nNomes em ordem alfabética:")
print(nomes[0])
print(nomes[1])
print(nomes[2])