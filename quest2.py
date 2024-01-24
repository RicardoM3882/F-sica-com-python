def cal_velocidade(gotejamento, distancia_gotas):

    temp_entre_gotas = 1 / gotejamento

    velocidade = distancia_gotas / temp_entre_gotas
    
    return velocidade

gotejamento = float(input("qual e a taxa de gotejamento?"))
distancia_gotas = float(input("qual a distancia entre as gotas?"))

vel_caminhao = cal_velocidade(gotejamento, distancia_gotas)

print(f"A velocidade do caminhão é {vel_caminhao} metros por segundo.")