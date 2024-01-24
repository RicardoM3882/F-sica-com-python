def for_norm(m, a):
    g = 10
    return m * (g + a)
massa = float(input("Diga a massa do objeto em kg: "))
aceleracao = float(input("Diga qual é a aceleração do elevador em m/s²: "))
forca = for_norm(massa, aceleracao)
print("A força normal exercida sobre o objeto é de aproximadamente", forca," N.")