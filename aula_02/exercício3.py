lista = []
print("\nDigite 'fim' para encerrar.")

while True:
    adicionar = input("Digite uma fruta para adicionar à lista: ")
    if adicionar == "fim":
        break
    lista.append(adicionar)
print(lista)