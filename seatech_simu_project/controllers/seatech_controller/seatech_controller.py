from curses import keyname
import os
from controller import Robot, Motor, Camera, DistanceSensor, Keyboard

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)


class CameraReco(Camera):
    def __init__(self):
        super().__init__('camera')
        self.enable(64)
        self.recognitionEnable(samplingPeriod=50)
        self.__tracked_name = None

    def track_object(self, object_name):
        self.__tracked_name = object_name

    def is_tracked_object_present(self):
        objs = self.getRecognitionObjects()
        for obj in objs:
            if self.__tracked_name == obj.get_model().decode("utf-8"):
                self.__recognized_object = obj
                return True
        return False




class SeatechRobot(Robot):
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        self.camera = CameraReco()

    def run(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(MAX_SPEED)

    def Left(self):
        self.__leftMotor.setVelocity(0.5*MAX_SPEED)
        self.__rightMotor.setVelocity(MAX_SPEED)

    def Right(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(0.5*MAX_SPEED)

    def Stop(self):
        self.__leftMotor.setVelocity(0)
        self.__rightMotor.setVelocity(0)

    def recule(self):
        self.__leftMotor.setVelocity(-0.75*MAX_SPEED)
        self.__rightMotor.setVelocity(-MAX_SPEED)



    def detection_object(self):
        data = self.camera.getRecognitionObjects()

        for object in data:
            color = object.get_colors()
            print(color)
            taille = object.get_size()
            print(taille)

            if (color == [1, 0, 0]):
                print("Object detecte")
                robot.recule()
            elif (color == [0, 1, 0]):
                print("Attaque !")
                robot.run()

            else :
                robot.Right()

                
                #if (obj.get_position_on_image()==)
        

if __name__== '__main__':
    TIME_STEP = 64
    MAX_SPEED = 6.28

# create the Robot instance.
    robot = SeatechRobot()

# get a handler to the motors and set target position to infinity (speed control)
# set up the motor speeds at 10% of the MAX_SPEED.

    print("Hello, je suis un robot")
    keyboard = Keyboard()
    keyboard.enable(samplingPeriod=100)
    
    while robot.step(TIME_STEP) != -1:
        key = keyboard.getKey()
        robot.detection_object()
        #print(key)
        if key == keyboard.UP:
            print('Salut')
            robot.run()
        elif key == keyboard.LEFT:
            print('Gauche !!!')
            robot.Left()
        elif key == keyboard.RIGHT:
            print('Droite !!!')
            robot.Right()
        elif key == keyboard.DOWN:
            print('Stop!!!')
            robot.Stop()
    pass