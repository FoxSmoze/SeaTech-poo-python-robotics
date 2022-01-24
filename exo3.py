from abc import ABCMeta, abstractmethod

class Véhicule():
    def __init__(self):
        print("C'est un véhicule")
        
    pass

class Voiture(Véhicule):
    def __init__(self):
        print("C'est une voiture")

    pass

class Moto(Véhicule):
    def __init__(self):
        print("C'est une moto et ouais bg")

    pass

class Scootbite(Véhicule):
    def __init__(self):
        print("C'est une merde de scoot")

    pass

class Compétition(Véhicule):
    def __init__(self):
        print("Ah ! La c'est un véhicule de compet frérot")

    pass

class WRC(Voiture, Compétition):
    def __init__(self):
        print("Et ouais c'est Loeb qui a gagné le rallye de mont'carl")
        super().__init__()

    pass

class Laguna(Voiture):
    def __init__(self):
        print("Oh une laguna de ses mort")
        super().__init__()

    pass

class MotoGP(Moto, Compétition):
    def __init__(self):
        print("De sacré couilles mon pote")
        super().__init__()

    pass