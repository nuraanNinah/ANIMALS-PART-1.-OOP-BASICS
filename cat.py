class Cat(Animal):
    def __init__(self,name, sounds):
        super().__init__(name,sounds)
    def food(self):
        print(self.name + " " +"eats")

    def sound(self):
        print(self.sounds + " "+"meows")
cat1 =Cat("Stormy", "Cat")
cat1.food()  
cat1.sound()