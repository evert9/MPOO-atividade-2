class Disciplina:
    def __init__(self, nome, cargaHoraria, curso, sala):
        self.nome = nome
        self.professor = None
        self.cargaHoraria = cargaHoraria
        self.sala = sala
        self.curso = curso
        self.turma = []

    def addAluno(self, aluno):
        self.alunos.append(aluno)

    def removeAluno(self, aluno):
        self.alunos.remove(aluno)

    def mostrarTurma(self):
        turmaStr = ""
        for a in self.alunos:
            turmaStr = f"{a.nome}, "
        return turmaStr[:-2]
        
    def calcMedia(self, n1, n2):
        return (n1 + n2) / 2
    
    def getProfessor(self):
        return self.professor
    
    def setProfessor(self, professor):
        self.professor = professor

    def __str__(self):
        return f"{self.nome} | Professor: {self.professor.nome} | Carga Horária: {self.cargaHoraria} | Sala: {self.sala}"