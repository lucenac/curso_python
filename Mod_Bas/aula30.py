"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 69  # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_car_pass_rad1 = velocidade > RADAR_1
carro_pass_rad1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_rad1 = carro_pass_rad1 and vel_car_pass_rad1

if vel_car_pass_rad1:
    print('Velocidade passou no Radar 1')
    
if carro_multado_rad1:
    print('Carro multado no radar 1')