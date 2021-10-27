sair = False
while sair == False:
    Tipos_Materiais = ('Plástico, Metal, Vidro e Papel')
    Material = input('Qual tipo de material deseja reciclar: ')
    
    if Material == 'Plástico':
        print('Local para descarte de plástico: R. Minoro Toyoda, 120 - Vale Verde, Valinhos - SP, 13279-150')
        link = print('Site para mais informações: https://www.azreciclagem.com.br/')
    
    if Material == 'Metal':
       print('Local para descarte de metais: R. Isnard Otranto, 50 - Jardim Novo Campos Eliseos, Campinas - SP, 13060-412')
       link = print('Site para mais informações: https://www.azreciclagem.com.br/')
        
    if Material == 'Papel':
        print('Locl para descarte de papéis: Av. Ruy Rodriguez, 394 - Jardim Novo Campos Eliseos, Campinas - SP, 13060-192')
        link = print('Site para mais informações: https://papeisbarao.com.br/')
    
    if Material == 'Vidro':
        print('Local para descarte de vidro: Av. Santa Isabel, 2300 - Barão Geraldo, Campinas - SP, 13084-012')
        link = print('Site para mais informações: http://www.campinas.sp.gov.br/governo/servicos-publicos/ecopontos/index.php')

    teste = input('Deseja continuar? Sim, Não: ')
    if teste == 'Não':
        sair = True