from abc import ABC, abstractmethod
from datetime import datetime


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if self._valor > 0:
            conta._saldo += self._valor
            conta._historico.adicionar_transacao(f"""Depósito: R$ {
                self._valor:.2f} - {datetime.now()}""")
        else:
            print("Valor de depósito inválido.")


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if self._valor > conta._saldo:
            print("Saldo insuficiente")
        elif self._valor > conta._limite:
            print(f"Valor do saque excede o limite de R$ {conta._limite:.2f}.")
        elif conta._limite_saques <= 0:
            print("Limite de saques diários atingido.")
        else:
            conta._saldo -= self._valor
            conta._limite_saques -= 1
            conta._historico.adicionar_transacao(f"""Saque: R$ {
                self._valor:.2f} - {datetime.now()}""")
            print(f"Saque de R$ {self._valor:.2f} realizado com sucesso.")


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    @property
    def transacoes(self):
        return self._transacoes


class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @property
    def agencia(self):
        return self._agencia

    def sacar(self, valor):
        saque = Saque(valor)
        saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

    @staticmethod
    def nova_conta(cliente, numero):
        return ContaCorrente(cliente, numero)


class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self._limite = 500.0
        self._limite_saques = 3

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    @limite_saques.setter
    def limite_saques(self, valor):
        self._limite_saques = valor


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf.replace(".", "").replace("-", "")

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento


def criar_cliente(nome, data_nascimento, cpf, endereco):
    return PessoaFisica(nome, data_nascimento, cpf, endereco)


def criar_conta_corrente(cliente, numero_conta):
    conta = ContaCorrente(cliente, numero_conta)
    cliente.adicionar_conta(conta)
    return conta


def exibir_extrato(conta):
    print("\n--- Extrato ---")
    if len(conta.historico.transacoes) == 0:
        print("Nenhuma transação realizada.")
    else:
        for transacao in conta.historico.transacoes:
            print(transacao)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")
    print("-----------------\n")


def menu():
    clientes = []
    numero_conta_sequencial = 1

    while True:
        print("----- Sistema Bancário -----")
        print("1. Criar Cliente")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Criar cliente
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (apenas números): ")
            endereco = input("""Endereço (logradouro, número - bairro - cidade/
                             estado): """)
            cliente = criar_cliente(nome, data_nascimento, cpf, endereco)
            clientes.append(cliente)
            print(f"Cliente {nome} criado com sucesso.")

        elif opcao == '2':  # Criar conta corrente
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                conta = criar_conta_corrente(cliente, numero_conta_sequencial)
                numero_conta_sequencial += 1
                print(f"""Conta criada para o cliente {cliente.nome}. Número
                      da conta: {conta.numero}.""")
            else:
                print("Cliente não encontrado.")

        elif opcao == '3':  # Depositar
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in cliente.contas if
                              conta.numero == numero_conta), None)
                if conta:
                    valor = float(input("Informe o valor do depósito: R$ "))
                    cliente.realizar_transacao(conta, Deposito(valor))
                else:
                    print("Conta não encontrada.")
            else:
                print("Cliente não encontrado.")

        elif opcao == '4':  # Sacar
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in cliente.contas if
                              conta.numero == numero_conta), None)
                if conta:
                    valor = float(input("Informe o valor do saque: R$ "))
                    cliente.realizar_transacao(conta, Saque(valor))
                else:
                    print("Conta não encontrada.")
            else:
                print("Cliente não encontrado.")

        elif opcao == '5':  # Exibir extrato
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in cliente.contas if
                              conta.numero == numero_conta), None)
                if conta:
                    exibir_extrato(conta)
                else:
                    print("Conta não encontrada.")
            else:
                print("Cliente não encontrado.")

        elif opcao == '6':  # Sair
            print("Encerrando o sistema bancário...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
