from asyncio.base_futures import _FINISHED


saldo = 0
saques = 3

print("""
            BEM VINDO 

""")

cont = 0
while True:
    for deposito in saques:
        deposito = float(input("Digite quanto deseja depositar em reais R$  "))

    if deposito != saldo:
        saldo = (deposito + saldo)
        cont = deposito - saques
    else:
        print("Opção Inválida!!!")
    



