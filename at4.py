def coef_atr(atrito, normal):
    return atrito / normal
peso = float(input("Diga qual é o peso do objeto em N: "))
atrito = float(input("diga qual é a força de atrito necessaria para manter o objeto constante N: "))
normal = peso
coeficiente = coef_atr(atrito, normal)
print("O coeficiente de atrito entre as duas superfícies é de aproximadamente", coeficiente,".")