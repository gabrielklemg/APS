import os
#eu fiz um prototipo baseado em uma atividade q fizemos numa lista de exercicio 
# mas o importante é o "import os" e o "os.system('cls')" pra limpar a tela
op = 0
while op != 5:
    voltar = False
    print ("Menu de opções:")
    print ("1. Imposto")
    print ("2. Novo salário")
    print ("3. Classificação")
    op = int(input("Informe a opção desejada. "))
    if op == 1:
        os.system('cls')
        while voltar != True:
            sal = float(input("Qual o seu salário: "))
            if sal < 500:
                print ("O imposto referente ao seu salário é de R$", sal*0.05)
            elif (sal >= 500) and (sal <= 850): 
                print ("O imposto referente ao seu salário é de R$", sal*0.10)
            elif sal > 850: 
                print ("O imposto referente ao seu salário é de R$", sal*0.15)
            print ("1.Continuar aqui. ")
            print ("2.Voltar ao menu. ")
            op = int(input("Informe a opção desejada. "))
            if op == 2:
                voltar = True
                os.system('cls')
            elif op == 1:
                os.system('cls')
            else:
                print ("Opção inválido")
                
    elif op == 2:
        os.system('cls')
        while voltar != True:
            sal = int(input("Qual o seu salário: "))
            if (sal > 1500.00): 
                print ("Seu novo salário é de R$", sal+25.00)
            elif (sal >=  750.00) and (sal <= 1500.00):
                print ("Seu novo salário é de R$", sal+50.00)
            elif (sal >=  450.00) and (sal <=  750.00):
                print ("Seu novo salário é de R$", sal+75.00)
            elif (sal < 450.00): 
                print ("Seu novo salário é de R$", sal+100.00)
            print ("1.Continuar aqui. ")
            print ("2.Voltar ao menu. ")
            op = int(input("Informe a opção desejada. "))
            if op == 2:
                voltar = True
                os.system('cls')
            elif op == 1:
                os.system('cls')
            else:
                print ("Opção inválido")

    elif op == 3:
        os.system('cls')
        while voltar != True:
            sal = int(input("Qual o seu salário: "))
            if (sal < 700): 
                print ("Mal remunerado.")
            elif(sal > 700): 
                print ("Bem remunerado.")
            print ("1.Continuar aqui. ")
            print ("2.Voltar ao menu. ")
            op = int(input("Informe a opção desejada. "))
            if op == 2:
                voltar = True
                os.system('cls')
            elif op == 1:
                os.system('cls')
            else:
                print ("Opção inválido")

    else:
        print ("Opção inválido")
