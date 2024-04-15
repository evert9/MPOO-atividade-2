class Aluno():
    def __init__(self, nome, matricula, curso, endereco, email):
        self.nome = nome
        self.__matricula = matricula
        self.curso = curso
        self.__endereco = endereco
        self.email = email
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

    def getEndereco(self):
        return self.__endereco
    
    def setEndereco(self, endereco):
        self.__endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}\nMatricula: {self.__matricula}\nCurso: {self.curso}\nEmail: {self.email}\nDisciplinas: {self.mostrarDisciplinas()}"