from Aluno import Aluno
from Professor import Professor
from Disciplina import Disciplina
from Curso import Curso
from Endereco import Endereco
from Curso import Curso
from Sala import Sala

cursoSI = Curso("Sistemas de Informação", 1234, 10)
cursoEngCivil = Curso("Engenharia Civil", 5678, 8)
cursoDireito = Curso("Direito", 9012, 9)
cursoAdmin = Curso("Administração", 3456, 7)
cursoMedicina = Curso("Medicina", 7890, 12)

enderecoAluno1 = Endereco(43, "Bairro das Flores", "Ao lado do mercado", "Centro", "Triunfo", "PE", "55566-0")
enderecoAluno2 = Endereco(22, "Rua Principal", "Próximo ao parque", "Centro", "Triunfo", "PE", "55555-0")
enderecoAluno3 = Endereco(55, "Avenida Central", "Perto da escola", "Centro", "Triunfo", "PE", "55554-0")
enderecoAluno4 = Endereco(10, "Rua das Flores", "Em frente ao mercado", "Centro", "Triunfo", "PE", "55553-0")
enderecoAluno5 = Endereco(7, "Rua do Comércio", "Próximo à praça", "Centro", "Triunfo", "PE", "55552-0")

enderecoProfessor1 = Endereco(11, "Rua Redonda", "Perto do banco", "Centro", "Recife", "PE", "77744-5")
enderecoProfessor2 = Endereco(15, "Rua do Bosque", "Próximo à academia", "Centro", "Recife", "PE", "77777-5")
enderecoProfessor3 = Endereco(30, "Avenida das Palmeiras", "Ao lado do parque", "Centro", "Recife", "PE", "77778-5")
enderecoProfessor4 = Endereco(8, "Rua da Praia", "Em frente ao mar", "Centro", "Recife", "PE", "77779-5")
enderecoProfessor5 = Endereco(25, "Rua das Montanhas", "Próximo à estação", "Centro", "Recife", "PE", "77780-5")

aluno1 = Aluno("Mario", "112-341", cursoSI, enderecoAluno1, "MarioMa@gmail.com")
aluno2 = Aluno("João", "222-342", cursoEngCivil, enderecoAluno2, "joao@gmail.com")
aluno3 = Aluno("Maria", "333-343", cursoDireito, enderecoAluno3, "maria@gmail.com")
aluno4 = Aluno("Pedro", "444-344", cursoAdmin, enderecoAluno4, "pedro@gmail.com")
aluno5 = Aluno("Laura", "555-345", cursoMedicina, enderecoAluno5, "laura@gmail.com")

professor1 = Professor("Ana", "Ana123@gmail.com", enderecoProfessor1)
professor2 = Professor("Carlos", "carlos@gmail.com", enderecoProfessor2)
professor3 = Professor("Juliana", "juliana@gmail.com", enderecoProfessor3)
professor4 = Professor("Lucas", "lucas@gmail.com", enderecoProfessor4)
professor5 = Professor("Mariana", "mariana@gmail.com", enderecoProfessor5)

sala1 = Sala(1, 40, "Bloco 01")
sala2 = Sala(2, 30, "Bloco 01")
sala3 = Sala(3, 35, "Bloco 02")
sala4 = Sala(4, 40, "Bloco 02")
sala5 = Sala(5, 35, "Bloco 03")

disciplinaCalculo = Disciplina("Calculo 1", 60, cursoSI, sala1)
disciplinaFisica = Disciplina("Física 1", 60, cursoEngCivil, sala2)
disciplinaPortugues = Disciplina("Português", 45, cursoDireito, sala3)
disciplinaEconomia = Disciplina("Economia", 60, cursoAdmin, sala4)
disciplinaAnatomia = Disciplina("Anatomia Humana", 90, cursoMedicina, sala5)

professor1.atribuirDisciplina(disciplinaCalculo)
professor2.atribuirDisciplina(disciplinaFisica)
professor3.atribuirDisciplina(disciplinaPortugues)
professor4.atribuirDisciplina(disciplinaEconomia)
professor5.atribuirDisciplina(disciplinaAnatomia)

aluno1.matricular(disciplinaCalculo)
aluno1.matricular(disciplinaFisica)
aluno1.matricular(disciplinaEconomia)

aluno2.matricular(disciplinaCalculo)
aluno2.matricular(disciplinaFisica)

aluno3.matricular(disciplinaPortugues)
aluno3.matricular(disciplinaEconomia)

aluno4.matricular(disciplinaCalculo)
aluno4.matricular(disciplinaEconomia)

aluno5.matricular(disciplinaAnatomia)

print("ALUNOS")
print(aluno1)
print("")
print(aluno2)
print("")
print(aluno3)
print("")
print(aluno4)
print("")
print(aluno5)
print("")

print("PROFESSORES")
print(professor1)
print("")
print(professor2)
print("")
print(professor3)
print("")
print(professor4)
print("")
print(professor5)
print("")
