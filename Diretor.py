from Servidor import Servidor

class Diretor(Servidor):
    def __init__(self, nome, endereco, email):
        super().__init__(nome, endereco, email)
        
    def calcSalario(self):
        salarioTotal = self.SALARIO_BASE * 6
        return salarioTotal

