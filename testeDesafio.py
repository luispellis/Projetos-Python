saldo = 0


print("Bem Vindo ao banco digital \n\n\n\n [1] Entrar \n [0] Sair")
opcao = int(input("Digite uma das duas opção: ")) 
while True:
    if opcao == 1:
        print("\n\n\n       Bem Vindo       \n\n\n [1] Depositar \n\n [2] Sacar  \n\n [3] Extrato  \n\n [0] Sair")
        opcaoMenu = int(input("O que deseja fazer ?: "))
        if opcaoMenu == 1:
            print("\n\n     Hora de Depositar   \n\n\n")
            deposito = float(input("Quanto deseja depositar?: "))
            saldo += deposito
            print(saldo)
        elif opcaoMenu == 2:
            print("")
        elif opcaoMenu == 3:
            print("")
        elif opcaoMenu == 0: 
            print("")
        else:
            print("Opção Inválida!!!")

    elif opcao == 0:
        break

    else:
        print("Opção Inválida!!!")