usuarios = []
contas = []
numero_conta_sequencial = 1


def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = cpf.replace(".", "").replace("-", "")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: Usuário com este CPF já cadastrado.")
            return

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"Usuário {nome} cadastrado com sucesso.")


def criar_conta_corrente(cpf_usuario):
    global numero_conta_sequencial
    cpf_usuario = cpf_usuario.replace(".", "").replace("-", "")

    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:

            contas.append({
                "agencia": "0001",
                "numero_conta": numero_conta_sequencial,
                "usuario": usuario
            })
            print(f"""Conta {numero_conta_sequencial} criada para o usuário
                  {usuario['nome']}.""")
            numero_conta_sequencial += 1
            return
    print("Erro: Usuário não encontrado. Verifique o CPF.")


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(f"Valor do saque excede o limite de R$ {limite:.2f} por saque.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n--- Extrato da Conta ---")
    if len(extrato) == 0:
        print("Nenhuma transação realizada.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("------------------------\n")


def menu():
    saldo = 0.0
    extrato = []
    limite_saques = 3
    numero_saques = 0
    limite_saque = 500.0

    while True:
        print("----- Sistema Bancário -----")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (apenas números): ")
            endereco = input("""Endereço (logradouro, número - bairro - cidade/
                             sigla do estado): """)
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == '2':
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(cpf)

        elif opcao == '3':
            valor = float(input("Digite o valor do depósito: R$ "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == '4':
            valor = float(input("Digite o valor do saque: R$ "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato,
                                   limite=limite_saque,
                                   numero_saques=numero_saques,
                                   limite_saques=limite_saques)

        elif opcao == '5':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '6':
            print("Encerrando sistema bancário...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
