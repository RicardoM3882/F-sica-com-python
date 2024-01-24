def acel_plano_incli(aplicada, atrito, normal, massa, angulo):
    g = 10
    for_pe = massa * g
    ang_rad = angulo * (3.14159 / 180)
    for_par = for_pe * ang_rad
    for_resul = aplicada - atrito - for_par
    aceleracao = for_resul / massa
    return aceleracao
aplicada = float(input("DIga qual é a força aplicada em N: "))
atrito = float(input("Diga qual é a força de atrito em N: "))
normal = float(input("Diga qual é a força normal em N: "))
massa = float(input("Diga qual é a massa do objeto em kg: "))
angulo = float(input("Digite o ângulo de inclinação do plano em graus: "))
aceleracao = acel_plano_incli(aplicada, atrito, normal, massa, angulo)
print("A aceleração do objeto é de aproximadamente", aceleracao," m/s².")