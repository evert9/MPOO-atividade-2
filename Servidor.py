from abc import abstractmethod
from Pessoa import Pessoa

class Servidor(Pessoa):
    __codigoAtual = 0

    def __init__(self, nome, endereco, email):
        super().__init__(nome, endereco, email)
        self.__codigo = Servidor.proximoCodigo()
        self.SALARIO_BASE = 1.412

    # LEMBRAR: self = método de instância / cls = método de classe
    @classmethod
    def proximoCodigo(cls):
        cls.__codigoAtual += 1
        return cls.__codigoAtual

    def getCodigo(self):
        return self.__codigo

    @abstractmethod
    def calcSalario(self):
        pass