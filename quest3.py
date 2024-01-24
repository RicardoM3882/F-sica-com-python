def calcular_velocidade_media_ultimo_trecho(dist_total, tempo_total, dist_primeiro_trecho, velo_primeiro_trecho, dist_segundo, velo_segundo_trecho):

    tempo_primeiro_trecho = dist_primeiro_trecho / velo_primeiro_trecho
    tempo_segundo_trecho = dist_segundo / velo_segundo_trecho
    
    tempo_ultimo_trecho = tempo_total - (tempo_primeiro_trecho + tempo_segundo_trecho)
    
    distancia_ultimo_trecho = dist_total - (dist_primeiro_trecho + dist_segundo)
    
    velocidade_media_ultimo_trecho = distancia_ultimo_trecho / tempo_ultimo_trecho
    
    return velocidade_media_ultimo_trecho

dist_total = float(input("qual a distancia total? "))
tempo_total = float(input("qual e o tempo total? "))
dist_primeiro_trecho = float(input("qual a distancia no primeiro trecho? "))
velo_primeiro_trecho = float(input("qual a velocidade no primeio trecho? "))
dist_segundo = float(input("qual a distancia no segundo trecho? "))
velo_segundo_trecho = float(input("qual a velocidade no segundo trecho? "))

velocidade_media_ultimo_trecho = calcular_velocidade_media_ultimo_trecho(dist_total, tempo_total, dist_primeiro_trecho, velo_primeiro_trecho, dist_segundo, velo_segundo_trecho)

print(f"A velocidade média no último trecho da viagem foi de {velocidade_media_ultimo_trecho} km/h.")
