class Professor:
    def __init__(self, nome,  email, endereco):
        self.nome = nome
        self.email = email
        self.__endereco = endereco
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
        
    def mostrarCusos(self):
        cursoStr = ""
        for c in self.cursos:
            cursoStr = f"{c.nome}, "
        return cursoStr[:-2]

    def getEndereco(self):
        return self.__endereco
    
    def setEndereco(self, endereco):
        self.__endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nDisciplias: {self.mostrarDisciplinas()}"