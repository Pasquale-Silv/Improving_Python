class Conto_Bancario():
    def __init__(self, nome, cognome, sommaIniziale):
        self.nome = nome
        self.cognome = cognome
        self.saldo = sommaIniziale

    def deposito(self, sommaDepositata):
        self.saldo += sommaDepositata

    def prelievo(self, sommaDaPrelevare):
        if (self.saldo < sommaDaPrelevare):
            return None
        elif(self.saldo >= sommaDaPrelevare):
            self.saldo -= sommaDaPrelevare
    