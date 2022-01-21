import time

class Robot():



    def __init__(self, name = '<unnamed>'):
        if name:
            self.__name = name
        self.__state = False
        self.__battery = 100
        self.__speed = 0
        self.__max_speed = 100      #on limite la vitesse du robot
        self.__time_action = None       #variable de temps enregistrée au début de chaque action


    #Renommé name si pas fait a l'initialisation
    def rename(self, name):
        if self.__name == "<unnamed>":
            self.__name = name
        else:
            print(f"""{self.__name} can't change his name""")



    #Allumé Robot
    def power_on(self):
        self.__time_action = time.time()
        if self.__state:
            print(f"""{self.__name} is already ON""")
        elif self.__battery == 0:
            print(f"""No Battery""")
        else :
            self.__state = True
            print(f"""{self.__name} ignition""")






    """
      Give your best code here ( •̀ ω •́ )✧
    """