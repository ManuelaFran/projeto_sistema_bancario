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
