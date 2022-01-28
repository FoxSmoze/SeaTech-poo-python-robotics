from abc import ABC, ABCMeta, abstractmethod

class Véhicule(ABC):
    def demarrer(self): 
        pass

class Voiture(Véhicule):
    def demarrer(self):
        print("C'est une voiture")
        pass

class Moto(Véhicule):
    def demarrer(self):
        print("C'est une moto eeeeh ouais bg ca se demarre au cick")
        pass

class Scootbite(Véhicule):
    def demarrer(self):
        print("C'est une merde de scoot")
        pass

class Compétition(Véhicule):
    def compet(self):
        print("Ah ! La c'est un véhicule de compet frérot, il faut un lanceur")
        pass

class Laguna(Voiture):
    def lag(self):
        print("Oh une laguna de ses mort")
        pass

class Demolitionderby(Voiture):
    def demolir(self):
        print("Demoooolitionnn !!!!")
        pass

class Rallye(Compétition, Voiture):
    def wrc(self):
        print("Et ouais c'est Loeb qui a gagné le rallye de mont'carl")
        pass

class MotoGP(Moto, Compétition):
    def ktm(self):
        print("De sacré couilles mon pote")
        pass

class FinDeVie(Laguna, Demolitionderby):
    def mort(self):
        print("Jamais sucée l'auto ses mort")
        pass


MonteCarlo = Rallye()
Bouillave = FinDeVie()
FabioQuatarraro = MotoGP()

MonteCarlo.demarrer()
MonteCarlo.compet()
MonteCarlo.wrc()

