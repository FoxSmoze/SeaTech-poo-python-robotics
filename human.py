class Human():
    __sexe = '<unnamed>'


#Constructor
    def __init__ (self, sexe=None):
        if sexe:
            self.__sexe = sexe


#Destructor
    def __del__(self):
        print("Auto destruction NOW")
    
#Manger
    def manger(self,aliments):
        for i in aliments:
            print("Vous avez mangé: %s aliments", aliments[i])


#
