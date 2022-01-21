from robot import Robot
from human import Human

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)


cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
#print('Charging battery...')
#cyborg.charge()
cyborg.status()
cyborg.manger('banana')
cyborg.manger(['coca', 'chips'])
print("Cyborg a mangé %s aliments" %cyborg.estomac)