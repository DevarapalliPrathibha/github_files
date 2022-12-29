class Car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)
carObj = Car()
carObj.sample_car_instance_method("hello again!")
carObj2 = Car()
carObj2.sample_car_instance_method(2)
print("\n")
class CarSample:
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,colour,name):
        self.colour = colour
        self.name = name
    def displayCarDetails(self):
        print(self.colour)
        print(self.name)
carObj = CarSample("black","Audi")
carObj.displayCarDetails()
print("\n")
#static method    (in static decoratives are used for defining every function & object is optional for both static and class)
class staticclass:
    @staticmethod
    def sample_static_method_substraction(a,b):
        print(a-b)
        return a-b
    @staticmethod
    def sample_static_method_addition(a,b):
        print(a+b)
        return a+b
                                                      # with obj :staticobj=staticclass
staticclass.sample_static_method_substraction(10,2)   #add=staticobj.method()
staticclass.sample_static_method_addition(10,2)
print("\n")                                          #print(add,sub)print("\n")
#class method
class Pinky:
    class1 = "hi"
    class2 = "hello"
    @classmethod
    def sample(cls):
        cls.class1 = "pavi"
        cls.class2 = "yamini"
Pinky.sample()                  #with obj=(classObj=pinky()
print(Pinky.class1)             #     var=(classobj.sample()
print(Pinky.class2)
print("\n")
#attributes and methods
class car:
    def __init__(self,colour,max_speed,acceleration,tyre_friction,current_speed):
        self.colour = colour
        self.max_speed = max_speed
        self.accerelation = acceleration
        self.tyre_friction = tyre_friction
        self.start_engine  = False
        self.current_speed = current_speed
    def stop_engine(self):
        self.start_engine = False
        print("engine stopped")
    def start_Engine(self):
        self.start_engine = True
        print("engine started")
    def acceleration(self,speed):
        self.speed = speed
        if self.current_speed >= self.max_speed:
            print("maximum speed reached")
        else:
            self.current_speed += speed
            print(self.current_speed)
    def apply_breaks(self,tyre_friction):
        self.tyre_friction = tyre_friction
        if self.current_speed == 0:
            print("breaks can not be applied")
        else:
            self.current_speed -= self.tyre_friction
            print("breaks are applied")
carObj = car("black",120,80,60,40)
carObj.start_Engine()
carObj.stop_engine()
carObj.acceleration(50)
carObj.apply_breaks(15)
    #def apply_breaks(self):











