import math


def distance(origin, destination):
    lat1, long1 = origin #definindo a latitute e logintute do ponto 1
    lat2, long2 = destination #definindo a latitute e logintute do ponto 2
    radius = 6371 #raio da terra

    #tranformando a diferença das latitute em radianos
    dlat = math.radians(lat2-lat1)
    
    #tranformando a diferença das longitute em radianos
    dlon = math.radians(long2-long1)
    
    #seno elevado a 2 da diferença da latitute dividido por 2
    #mais coseno da latitute 1 vezes coseno da latitute 2 vezes seno elevado a 2 da diferença da logintute dividido por 2
    a = math.sin(dlat/2) **2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) **2

    # 2 vezes o arco seno da raiz quadrada de a
    c = 2 * math.asin(math.sqrt(a))

    # raio da terra vezes c
    d = radius * c

    return d

origin = (-22.907370,-47.062901) #campinas
destination =(-22.883140,-47.210920) #hortolândia
print("A distância em KM : {} ".format(distance(origin, destination)))
    
#só um prototipo,usando a fórmula de haversine
#como eu disse isso é a distância em linha reta
#e se vc roda esse código vai dar 15.39 km e se procurar a distância
#em linha reta entre as 2 cidades vai ver q é 17.01,
#esse fórmula tem uma margem de erro pq usa o raio da terra
#e a terra ñ é uma esfera perfeita
#link do wiki sobre essa formula se quiserem entender melhor o calculo
#https://pt.wikipedia.org/wiki/F%C3%B3rmula_de_haversine
