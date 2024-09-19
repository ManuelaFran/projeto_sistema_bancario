menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0.0
depositos = []
saques = []
limite_saque_diario = 3
saque_maximo = 500.0
saques_diarios_realizados = 0

while True:
    print("----- Sistema Bancário -----")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':  # Depósito
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            depositos.append(valor_deposito)
            print(f"""Depósito de R$ {valor_deposito:.2f}
                  realizado com sucesso.""")
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    elif opcao == '2':  # Saque
        if saques_diarios_realizados >= limite_saque_diario:
            print("Você já realizou o limite máximo de saques diários.")
        else:
            valor_saque = float(input("Digite o valor do saque: R$ "))
            if valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor_saque > saque_maximo:
                print(f"""Valor do saque excede o limite de R$
                      {saque_maximo:.2f} por saque.""")
            elif valor_saque > 0:
                saldo -= valor_saque
                saques.append(valor_saque)
                saques_diarios_realizados += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            else:
                print("Valor de saque inválido. Insira um valor positivo.")
