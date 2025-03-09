


class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def eat(self) :
        print(f"{self.name} is eating.")    
    def sleep(self) :
        print(f"{self.name} is sleeping.")  
class Sheep(Animal) :
    def wool(self):
        print(f"{self.name} gives wool.")
class Cow(Animal) :
    def milk(self):
        print(f"{self.name} gives milk.")
class Chicken(Animal) :
    def egg(self) :
        print(f"{self.name} gives an egg.") 

sheep = Sheep("Carl", 5)
cow = Cow("Linda", 3)
chicken = Chicken("Anny", 1)      

sheep.sleep()
cow.milk()