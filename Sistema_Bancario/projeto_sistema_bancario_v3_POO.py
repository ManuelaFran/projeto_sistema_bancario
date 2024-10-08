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