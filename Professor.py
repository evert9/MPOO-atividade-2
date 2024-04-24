from Servidor import Servidor

class Professor(Servidor):
    def __init__(self, nome, endereco,  email):
        super().__init__(nome, endereco, email)
        self.disciplinas = []
        self.cursos = []

    def atribuirDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        disciplina.setProfessor(self)

    def removerDisciplina(self, disciplina):
        self.disciplinas.remove(disciplina)

    def mostrarDisciplinas(self):
        disciplinasStr = ""
        for d in self.disciplinas:
            disciplinasStr = f"{d.nome}, "
        return disciplinasStr[:-2]
        
    def mostrarCursos(self):
        cursoStr = ""
        for c in self.cursos:
            cursoStr = f"{c.nome}, "
        return cursoStr[:-2]

    def calcSalario(self):
        salarioTotal = self.SALARIO_BASE * 4
        return salarioTotal

    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nDisciplias: {self.mostrarDisciplinas()}"