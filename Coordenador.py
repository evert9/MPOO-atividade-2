from Servidor import Servidor

class Coordenador(Servidor):
    def __init__(self, nome, endereco, email, curso):
        super().__init__(nome, endereco, email)
        self.curso = curso

    def atribuirCurso(self):
        self.curso.setCoordenador(self)

    def calcSalario(self):
        salarioTotal = self.SALARIO_BASE * 5
        return salarioTotal
    