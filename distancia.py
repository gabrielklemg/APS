from math import sin, cos, sqrt, atan2, radians #importando seno, coseno, raiz quadrada, tangente, radiano

def dis(p, vid):
    R = 6371.0 #Raio aproximado da terra

    lat1 = radians(p[0])
    lon1 = radians(p[1])
    lat2 = radians(vid[0])
    lon2 = radians(vid[1])

    dlon = lon2 - lon1 #terceira longitude
    dlat = lat2 - lat1 #terceira latitude para triangular a distância do ponto a ao ponto b

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2 #formula complexa para calcular a distâcia
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    dis = R * c

    return round(dis, 3)

p = (23, 46)
vid = (23, 46)

print("Você está a aproximadamente: ", dis(p, vid),"metros")