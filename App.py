from Aluno import Aluno
from Coordenador import Coordenador
from Professor import Professor
from Disciplina import Disciplina
from Curso import Curso
from Endereco import Endereco
from Curso import Curso
from Sala import Sala
from Diretor import Diretor  # type: ignore

cursoSI = Curso("Sistemas de Informação", 1234, 10)
cursoEngCivil = Curso("Engenharia Civil", 5678, 8)
cursoDireito = Curso("Direito", 9012, 9)
cursoAdmin = Curso("Administração", 3456, 7)
cursoMedicina = Curso("Medicina", 7890, 12)

enderecoAluno1 = Endereco(43, "Bairro das Flores",
                          "Ao lado do mercado", "Centro", "Triunfo", "PE", "55566-0")
enderecoAluno2 = Endereco(
    22, "Rua Principal", "Próximo ao parque", "Centro", "Triunfo", "PE", "55555-0")
enderecoAluno3 = Endereco(
    55, "Avenida Central", "Perto da escola", "Centro", "Triunfo", "PE", "55554-0")
enderecoAluno4 = Endereco(
    10, "Rua das Flores", "Em frente ao mercado", "Centro", "Triunfo", "PE", "55553-0")
enderecoAluno5 = Endereco(
    7, "Rua do Comércio", "Próximo à praça", "Centro", "Triunfo", "PE", "55552-0")

enderecoDiretor = Endereco(
    10, "Rua Principal", "Próximo à praça", "Centro", "Triunfo", "PE", "55555-000")

enderecoCoordenador1 = Endereco(
    15, "Rua das Palmeiras", "Próximo ao mercado", "Centro", "Triunfo", "PE", "55555-555")
enderecoCoordenador2 = Endereco(
    25, "Avenida da Liberdade", "Ao lado do cinema", "Bairro Novo", "Triunfo", "PE", "55555-666")
enderecoCoordenador3 = Endereco(
    35, "Rua dos Professores", "Em frente à escola", "Vila São João", "Triunfo", "PE", "55555-777")
enderecoCoordenador4 = Endereco(
    45, "Avenida das Árvores", "Próximo ao parque", "Jardim Esperança", "Triunfo", "PE", "55555-888")
enderecoCoordenador5 = Endereco(
    55, "Rua do Sol", "Ao lado do museu", "Centro", "Triunfo", "PE", "55555-999")

enderecoProfessor1 = Endereco(
    11, "Rua Redonda", "Perto do banco", "Centro", "Recife", "PE", "77744-5")
enderecoProfessor2 = Endereco(
    15, "Rua do Bosque", "Próximo à academia", "Centro", "Recife", "PE", "77777-5")
enderecoProfessor3 = Endereco(30, "Avenida das Palmeiras",
                              "Ao lado do parque", "Centro", "Recife", "PE", "77778-5")
enderecoProfessor4 = Endereco(
    8, "Rua da Praia", "Em frente ao mar", "Centro", "Recife", "PE", "77779-5")
enderecoProfessor5 = Endereco(
    25, "Rua das Montanhas", "Próximo à estação", "Centro", "Recife", "PE", "77780-5")

aluno1 = Aluno("Mario", enderecoAluno1,
               "MarioMa@gmail.com", "112-341", cursoSI)
aluno2 = Aluno("João", enderecoAluno2, "joaoDoPenel@gmail.com",
               "222-342", cursoEngCivil)
aluno3 = Aluno("Maria", enderecoAluno3,
               "mariamada@gmail.com", "333-343", cursoDireito)
aluno4 = Aluno("Pedro", enderecoAluno4,
               "pedrogado@gmail.com", "444-344", cursoAdmin)
aluno5 = Aluno("Laura", enderecoAluno5, "lauranel@gmail.com",
               "555-345", cursoMedicina)

diretor = Diretor("Rogerio", enderecoDiretor, "rogeriogerio@gmail.com")

coordenador1 = Coordenador(
    "Luana", enderecoCoordenador1, "luavai@gmail.com", cursoSI)
coordenador2 = Coordenador(
    "Mariana", enderecoCoordenador2, "marianaBanana@gmail.com", cursoEngCivil)
coordenador3 = Coordenador(
    "Jose", enderecoCoordenador3, "josese@gmail.com", cursoDireito)
coordenador4 = Coordenador(
    "Carlos", enderecoCoordenador4, "carlinho@gmail.com", cursoAdmin)
coordenador5 = Coordenador(
    "Angela", enderecoCoordenador5, "angelada@gmail.com", cursoMedicina)

professor1 = Professor("Bruna", enderecoProfessor1, "AnaSkatista@gmail.com")
professor2 = Professor("Chico", enderecoProfessor2, "chicoDoArque@gmail.com")
professor3 = Professor("Juliana", enderecoProfessor3, "hooJuliana@gmail.com")
professor4 = Professor("Lucas", enderecoProfessor4, "lucasado@gmail.com")
professor5 = Professor("Rosa", enderecoProfessor5, "rosaMurcha@gmail.com")

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

print("DIRETOR")
print(diretor)
print(f"Salário: R${diretor.calcSalario()}")
print("")

print("COORDENADORES")
print(f"{coordenador1}\nCódigo: {coordenador1.getCodigo()}")
print("")
print(f"{coordenador2}\nCódigo: {coordenador2.getCodigo()}")
print("")
print(f"{coordenador3}\nCódigo: {coordenador3.getCodigo()}")
print("")
print(f"{coordenador4}\nCódigo: {coordenador4.getCodigo()}")
print("")
print(f"{coordenador5}\nCódigo: {coordenador5.getCodigo()}")
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
