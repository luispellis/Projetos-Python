
from time import sleep

saldoAtual = 0
valorMinimo = 1
saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3


#Interface com o usuário
InterfaceInicio = f''' 
     **************************************************************

                Seja Bem Vindo ao Banco Digital
        


                        press [1] enter


                                                        [0] Sair

    ***************************************************************
    '''

    

print(InterfaceInicio)
nome = str(input(">>>>>>>Digite seu nome:  "))
opcao = int(input(">>>>>>> Qual é a sua opção?: "))

while True:
    if opcao == 1:
        print("""
            *******************************************************

                          BEM-VINDO {}
           
                 {} Temos 3 opções disponíveis para você

             [1] Depositar

             [2] Saque

             [3] Extrato


            *******************************************************
                                                        [0] Sair
        """.format(nome,nome))
        opcaoMenu = int(input("\nO que deseja fazer {}? ".format(nome)))
        if opcaoMenu == 1:
                print(""" 
                \n\n
                ********************************************

                                DEPOSITAR


                ********************************************
                    """)
                saldo = valorDeposito = float(input("\nDigite o valor do seu depósito R$ "))
                valorDeposito += saldoAtual
                if valorDeposito > valorMinimo:
                    print("""

                    ********************************************
                    
                            **** Depositado com sucesso ****
                

                        [1] Saldo                  [0] Sair
               
                    ********************************************
                    """)
                    opcaoDeposito = int(input("\nO que deseja fazer {} ? ".format(nome)))
                    if opcaoDeposito == 1:
                        
                        print(""" 
                        *******************************************************

                    
                            {} O seu saldo atual é de: R$ {}


                                        Voltando ao ínicio . . .
                        
                        *******************************************************
                        
                        """.format(nome,valorDeposito))

                        sleep (3)
                
                    elif opcaoDeposito == 0:
                        break

                    else:
                        print("Opção inválida, tente novamente com as opções oferecidas!!! ") 
                else:
                    print(""" \n\n
                    
                    *******************************************************


                        NÃO É POSSIVEL DEPOSITAR R$ {}
                    
                     É preciso no min. R$ 1,00 para efetuar o depósito!!! 
                    
                    
                                            Voltando ao inicio . . . 

                    *******************************************************
                                            
                         """.format(valorDeposito)) 
                    sleep(3)

        elif opcaoMenu == 2:
                if saldo < valorMinimo:
                    print("""
                    *******************************************************
                    

                    O SEU SALDO É DE R$ {}, É NECESSÁRIO DEPOSITAR ALGUM VALOR PARA SACAR


                                                Voltando ao Menu ...

                    
                    *******************************************************
                    """.format(saldo))
                    sleep(3)
                else:   
                    print("""
                        *******************************************************        
                                
                                
                                 Bem Vindo ao saque rápido


                   
                        {} o limite é de 3 saques diários

                        O seu saldo é de R$ {}

                        *******************************************************
                    """.format(nome,saldoAtual))   
                    sacar = float(input("{} Digite o valor que deseja sacar: ".format(nome)))
                    saldoAtual = saldo - sacar
                    if sacar < valorMinimo:
                        ("""
                        ********************************************************

                            Valor indisponível, preencha um valor válido para saque
                            
                        ********************************************************
                        """)
                    elif sacar > limite:
                        print("""
                            ****************************************************

                            
                                    Valor máximo para saque excedido!!! 
                                    

                            ****************************************************        
                            """)
                    elif saldo < sacar:
                        print("""
                            ****************************************************

                                            Dinheiro indisponível !!!        
                                            
                                            
                            Tente novamente. 

                            ****************************************************

                            aguarde ...
                        
                            """)
                        print("Aguarde ...")
                        sleep(3)
                    else:
                        print("""     
                        ********************************************************
                        
                                    SAQUE REALIZADO COM SUCESSO !!!
                        



                        [1] Visualizar Saldo?                   [0] Sair
                        ********************************************************
                        """)
                    sleep(3)
                    opcao = int(input("O que deseja fazer? "))
                    if (opcao == 1):
                        print("""
                        ********************************************************

                            {} o seu saldo atual é de R$ {}
                        

                        Aguarde ...
                        ********************************************************
                        """.format(nome,saldoAtual))
                        sleep(3)
                    elif (opcao == 0):
                        break

                    else:
                        print("Opção inválida, tente novamente ...")
                        sleep(2)

        elif opcaoMenu == 3:
                print("")
        elif opcaoMenu == 0:
                break

        else:
                print("Opção inválida, por favor escolha uma opção!")

    elif opcao == 0:
        break