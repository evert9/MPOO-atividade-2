class Sala:
    def __init__(self, numero, capacidade, predio):
        self.numero = numero
        self.capacidade = capacidade
        self.predio = predio

    def upgradeNumero(self, newNum):
        self.numero = newNum

    def upgradeCapacidade(self, newCap):
        self.capacidade = newCap

    def __str__(self) -> str:
        return f"Número: {self.numero} Capacidade: {self.capacidade} Predio: {self.predio}"