menu = """
-------------------------------------------
Olá, qual a opereação que deseja fazer:    
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = "Operação - Valor\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = str(input('==> '))
    print('-------------------------------------------')
    if opcao == 'd':
        valor = float(input("Quanto deseja depositar: R$ "))
        saldo += valor
        extrato += f"Depósito - R${valor:.2f}\n"
        print("Processando...")
        print("Operação efetuada com sucesso!")
    elif opcao == 's':
        saque = float(input("Quanto deseja sacar: R$ "))
        print("Processando...")

        if (saldo - saque < 0):
            print("Operação Inválida: Quantia indisponível na conta")
        elif (saque > 500.00):
            print("Operação Inválida: O valor máximo de saque é R$ 500,00")
        elif (numero_saques >= LIMITE_SAQUES):
            print("Operação Inválida: Limite de saques diários atingido")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque - R${saque:.2f}\n"
            print("Operação efetuada com sucesso!")
    elif opcao == 'e':
        print(extrato)
        print(f"\nSaldo atual: R${saldo:.2f}")
    
    elif opcao == 'q':
        break

    else:
        print('Operação Inválida!')


