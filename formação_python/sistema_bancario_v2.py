# Variáveis globais
clientes = []
contas = []
cpfs = []
AGENCIA = "0001"

def menu_inicial():
    menu = """
-------------------------------------------
Olá, qual a operação que deseja fazer:
[1] Cadastrar novo usuário
[2] Cadastrar nova conta
[3] Acessar minha conta
[4] Sair

    """
    return menu

def menu_operacoes(usuario):
    for cliente in clientes:
        if usuario == cliente[2]:
            nome = cliente[0]
    menu = f"""
-------------------------------------------
Olá, {nome}!
Qual a operação que deseja fazer:    
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

    """
    return menu

def cadastrar_usuario():
    print("Digite algumas informações: ")
    nome = str(input("Nome: "))
    data = str(input("Data de Nascimento (DD-MM-AAAA): "))
    cpf = str(input("CPF: "))
    if cpf in cpfs:
        falha = "Usuário já cadastrado"
        return falha
    else:
        endereco = str(input("Endereço (Logradouro, número - Bairro - Cidade / UF): "))
        dados = (nome, data, cpf, endereco)
        clientes.append(dados)
        cpfs.append(cpf)
        sucesso = "Usuário cadastrado com sucesso"
        return sucesso

def cadastrar_conta(usuario):
    if usuario not in cpfs:
        err = 'Usuário não cadastrado'
        return err
    else:
        conta = str(len(contas) + 1)
        dados = (AGENCIA, conta, usuario)
        infos = f"""
        Dados da conta:
        Agência: {AGENCIA}
        Conta: {conta}
        Usuário: {usuario}

        Conta criada com sucesso!
        """
        contas.append(dados)
        return infos
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print("Processando...")

    if (saldo - valor < 0):
        return ("Operação Inválida: Quantia indisponível na conta")
    elif (valor > limite):
        return (f"Operação Inválida: O valor máximo de saque é R$ {limite:.2f}")
    elif (numero_saques >= limite_saques):
        return ("Operação Inválida: Limite de saques diários atingido")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque - R${valor:.2f}\n"
        print("Operação efetuada com sucesso!")
        return saldo, extrato, numero_saques
    
def depositar(saldo, valor, extrato, /):
    print("Processando...")

    saldo += valor
    extrato += f"Depósito - R${valor:.2f}\n"
    print("Operação efetuada com sucesso!")
    return saldo, extrato

def imprimir(saldo, /, *, extrato):
    print("Processando...")
    print(extrato)
    print(f"\nSaldo atual: R${saldo:.2f}")

def main():
    saldo = 0
    limite = 500
    extrato = "Operação - Valor\n"
    numero_saques = 0
    limite_saques = 3

    while True:
        print(menu_inicial())
        opcao = str(input('==> '))
        print('-------------------------------------------')
        if opcao == '1':
            print(cadastrar_usuario())
        elif opcao == '2':
            cpf = str(input("Digite o CPF do usuário: "))
            print(cadastrar_conta(cpf))
        elif opcao == '3':
            print('-------------------------------------------')
            agencia = str(input("Digite a agência: "))
            conta = str(input("Digite a conta: "))
            cpf = str(input("Digite o CPF do titular: "))
            print('-------------------------------------------')
            # TO DO: Ajeitar isso aqui
            if len(contas) == 0:
                print('Não existem clientes cadastrados')
            else:
                for cliente in contas:
                    if cliente[0] != agencia or cliente[1] != conta or cliente[2] != cpf:
                        print('Dados incorretos') 
                    else:
                        while opcao != 'q':
                            print(menu_operacoes(cpf))
                            opcao = str(input('==> '))
                            print('-------------------------------------------')
                            if opcao == 'd':
                                valor = float(input("Quanto deseja depositar: R$ "))
                                saldo, extrato = depositar(saldo, valor, extrato)
                            elif opcao == 's':
                                valor = float(input("Quanto deseja sacar: R$ "))
                                if type(sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)) == tuple:
                                    saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
                                else:
                                    print(sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques))
                            elif opcao == 'e':
                                imprimir(saldo, extrato=extrato)
                            
                            else:
                                print('Operação Inválida!')
        
        elif opcao == '4':
            break

        else:
            print('Operação Inválida!')

main()


