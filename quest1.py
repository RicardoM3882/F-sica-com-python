def comprimento_do_trem(velo, comp_ponte, tempo):

    velocidade = velo * (5/18)
    
    comprimento_trem = (velocidade * tempo) - comp_ponte
    
    return comprimento_trem

velo = float(input("qual a velocidade? "))
comp_ponte = float(input("qual o comprimento da ponte? "))
tempo = float(input("qual o tempo? "))

comprimento = comprimento_do_trem(velo, comp_ponte, tempo)

print(f"O comprimento do trem é {comprimento} metros.")
