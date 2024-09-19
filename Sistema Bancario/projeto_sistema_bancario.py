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
