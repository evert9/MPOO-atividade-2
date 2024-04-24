class Pessoa():
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.__endereco = endereco
        self.email = email

    def getEndereco(self):
        return self.__endereco
    
    def setEndereco(self, endereco):
        self.__endereco = endereco

    def __str__(self):
        if hasattr(self, 'curso'):
            return f"Nome: {self.nome}\nE-mail: {self.email}\nEndereço: {self.__endereco}\nCurso: {self.curso}"
        else:
            return f"Nome: {self.nome}\nE-mail: {self.email}\nEndereço: {self.__endereco}"
        