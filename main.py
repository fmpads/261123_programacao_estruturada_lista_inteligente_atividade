informacoes = []

for i in range(1, 6):
    entrada = input(f"DIGITE A {i}ª INFORMAÇÃO: ")

    try:
        valor = int(entrada)
    except ValueError:
        try:
            valor = float(entrada)
        except ValueError:
            valor = entrada

    informacoes.append(valor)

print("LISTA:")
print(informacoes)

print("TIPOS DE DADOS:")
for i, valor in enumerate(informacoes):
    tipo = type(valor).__name__
    if i < len(informacoes) - 1:
        print(f"{valor} - {tipo}; ", end="")
    else:
        print(f"{valor} - {tipo}.")