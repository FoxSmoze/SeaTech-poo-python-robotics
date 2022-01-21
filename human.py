import time


class Human():
    __sexe = '<unnamed>'
    __estomac = 0


    #Constructor
    def __init__ (self, sexe):
        if sexe:
            self.__sexe = sexe


    #Destructor
    def __del__(self):
        print("Auto destruction NOW")
    
    #Manger
    def manger(self,aliments):
        if type(aliments)==str:
            print("Vous avez mangé:", aliments)
            time.sleep(1)
            self.__estomac = self.__estomac + 1
        else:

            for i in aliments:
                print("Vous avez mangé: %s" %i)
                time.sleep(1)
                self.__estomac = self.__estomac + 1

    @property
    def sexe(self):
        return self.__sexe

    @property
    def estomac(self):
        return self.__estomac