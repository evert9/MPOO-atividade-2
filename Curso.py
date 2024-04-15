class Curso:
    def __init__(self, nome, codigo, duracao):
        self.nome = nome
        self.codigo = codigo
        self.duracao = duracao
        self.disciplinas = []
        self.alunos = []
        self.professores = []

    def mostarDisciplinas(self):
        disciplinasStr = ""
        for d in self.disciplinas:
            disciplinasStr += f"{d.nome}, "
        return disciplinasStr[:-2]
        
    def mostarAlunos(self):
        alunosStr = ""
        for a in self.alunos:
            alunosStr = f"{a.nome}, "
        return alunosStr[:-2]
    
    def mostarProfessores(self):
        professoresStr = ""
        for p in self.professores:
            professoresStr = f"{p}, "
        return professoresStr[:-2]
        
    def __str__(self):
        return f"{self.nome} | Código: {self.codigo} | Duração: {self.duracao} periodos"