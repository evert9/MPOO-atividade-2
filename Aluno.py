from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, endereco, email, matricula, curso):
        super().__init__(nome, endereco, email)
        self.__matricula = matricula
        self.curso = curso
        self.disciplinas = []

    def matricular(self, disciplina):
        self.disciplinas.append(disciplina)

    def removerMatricula(self, disciplina):
        self.disciplinas.remove(disciplina)

    def mostrarDisciplinas(self):
        disciplinasStr = ""
        for d in self.disciplinas:
            disciplinasStr += f"{d.nome}, "
        return disciplinasStr[:-2]

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}\nMatricula: {self.__matricula}\nCurso: {self.curso}\nEmail: {self.email}\nDisciplinas: {self.mostrarDisciplinas()}"
