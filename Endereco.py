class Endereco:
    def __init__(self, numero, bairro, complemento, logradouro, cidade, estado, cep):
        self.__numero = numero
        self.__bairro = bairro
        self.__complemento = complemento
        self.__logradouro = logradouro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    def atualizarDados(self, novoNumero, novoBairro, novoComplemento, novoLogradouro, novaCidade, novoEstado, novoCep):
        self.__numero = novoNumero
        self.__bairro = novoBairro
        self.__complemento = novoComplemento
        self.__logradouro = novoLogradouro
        self.__cidade = novaCidade
        self.__estado = novoEstado
        self.__cep = novoCep
        return "Dados do endereço atualizados com sucesso!"

    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero

    def get_bairro(self):
        return self.__bairro

    def set_bairro(self, bairro):
        self.__bairro = bairro

    def get_complemento(self):
        return self.__complemento

    def set_complemento(self, complemento):
        self.__complemento = complemento

    def get_logradouro(self):
        return self.__logradouro
    
    def set_logradouro(self, logradouro):
        self.__logradouro = logradouro

    def get_cidade(self):
        return self.__cidade
    
    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_cep(self):
        return self.__cep
    
    def set_cep(self, cep):
        self.__cep = cep

    def __str__(self):
        return f"Número: {self.__numero}, Bairro: {self.__bairro}, Cidade: {self.__cidade}, Estado: {self.__estado}"