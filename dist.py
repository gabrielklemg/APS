import math


def distancia(lat1, long1, lat2, long2):
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

#origin = (-22.907370,-47.062901) #campinas
#destination =(-22.883140,-47.210920) #hortolândia
#print("A distância em KM : {} ".format(distance(origin, destination)))
    
#só um prototipo,usando a fórmula de haversine
#como eu disse isso é a distância em linha reta
#e se vc roda esse código vai dar 15.39 km e se procurar a distância
#em linha reta entre as 2 cidades vai ver q é 17.01,
#esse fórmula tem uma margem de erro pq usa o raio da terra
#e a terra ñ é uma esfera perfeita
#link do wiki sobre essa formula se quiserem entender melhor o calculo
#https://pt.wikipedia.org/wiki/F%C3%B3rmula_de_haversine

#latitute e longitute do destino
matrizlo = [[[-82.883140, 107.210920],[-42.883140, 87.210920],[-22.883140, -47.210920]],[[-22.883140, -47.210920],[-122.883140, 147.210920],[-82.883140, 107.210920]],[[-2.883140, 17.210920],[-22.883140, -47.210920],[-52.883140, 67.210920]],[[-22.883140, -47.210920],[-12.883140, 37.210920],[-32.883140, 57.210920]],[[-82.883140, 167.210920],[-42.883140, 87.210920],[-22.883140, -47.210920]]]    
#nomes dos destinos
matrizlu = [['lugar1', 'lugar2', 'lugar3'],['lugar1', 'lugar2', 'lugar3'],['lugar1', 'lugar2', 'lugar3'],['lugar1', 'lugar2', 'lugar3'],['lugar1', 'lugar2', 'lugar3']]
#vetor q ira receber a distância
vetor = [0, 0, 0]
#vetor dos tipos de materias
vetor2 = ['papel', 'plástico', 'vidro', 'metal', 'madeira']

#latitute e longitute do ponto de partida dado pelo úsuario
print("Informe sua localização com base na latitude e longitude abaixo.")
x = float(input('Digite sua latitute: '))
y = float(input('Digite sua longitute: '))
for i in range(0, 5):
    #mostrando o material
    print("╭───────╯•╰───────╮\n")
    print(f'Material {vetor2[i]}\n')
    for j in range(0, 3):
        #fazendo o calculo da distância e colocando no vetor, quando o i mudar vai mudar de material o vetor vai receber os novos valores
        vetor[j] = distancia(x, y, matrizlo[i][j][0], matrizlo[i][j][1])
        #mostrando a distância
        print(f'┃➲ A distância é {vetor[j]:.2f} km')
    for j in range(0, 2):
        for c in range(j+1, 3):
            #organizando o vetor e a matriz dos lugares para que o com a menor distãncia fica na frente
          if vetor[j] > vetor[c]:
              aux1 = vetor[j]
              vetor[j] = vetor[c]
              vetor[c] = aux1
              aux2 = matrizlu[i][j]
              matrizlu[i][j] = matrizlu[i][c]
              matrizlu[i][c] = aux2
            #mostrando o local com menor distância
    print(f'O lugar mais próximo é o {matrizlu[i][0]} com {vetor[0]:.2f} km de distância.\n')
    print("╰───────╮•╭───────╯")
