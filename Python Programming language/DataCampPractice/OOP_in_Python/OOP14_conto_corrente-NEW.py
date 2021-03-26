class Conto:
    def __init__(self, nome, sommaIniziale):
        self.nome = nome
        self.sommaIniziale = sommaIniziale

    def versamento(self, sommaDaVersare):
        self.sommaIniziale += sommaDaVersare

    def prelievo(self, sommaDaPrelevare):
        if(self.sommaIniziale < sommaDaPrelevare):
            print("Impossibile prelevare, lei non dispone di abbastanza fondi")
        else:
            self.sommaIniziale -= sommaDaPrelevare

pasquale = Conto("Pasquale", 5000)

print(pasquale.sommaIniziale)
pasquale.prelievo(1500)
print(pasquale.sommaIniziale)

pasquale.versamento(100000)
print(pasquale.sommaIniziale)

pasquale.prelievo(500000)
print(pasquale.sommaIniziale)