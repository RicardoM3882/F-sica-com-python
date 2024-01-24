def for_atr(atrito, normal):
    return atrito * normal
coeficiente = float(input("qual é o coeficiente de atrito: "))
for_norm = float(input("Digite a força normal exercida sobre o objeto: "))
for_atr = for_atr(coeficiente, for_norm)
print("A força de atrito necessária para manter o objeto em repouso é de ", for_atr," N.")