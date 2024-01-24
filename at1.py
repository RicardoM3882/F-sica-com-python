def for_norm(massa, gravidade):
    gravidade = 10
    return massa * gravidade
massa = float(input("qual e a massa do objeto em kg: "))
angulo = float(input("Diga qual é o ângulo de inclinação do plano em graus: "))
forca = for_norm(massa, angulo)
print("A força normal exercida sobre o objeto é de +-", forca,"  N.")