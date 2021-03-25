class Home:
    def __init__(self, pets = []):
        self.pets = pets
    def Adopt_pets(self, pet):
        for each in self.pets:
            if each == pet:
                raise Exception ("you cann't adopt 2 pets")
        self.pets.append(pet)


def makeAllSounds(self):
        for animal in self.__pets:
            animal.sound()
            
def main():
    home = Home()
    dog1 = Dog()
    dog2 = Dog()
    cat = Cat()
    

    dog1 = Dog("Rax", "barks")
    cat1 = Cat("Stormy", " meows")
    home.Adopt_pets(dog1)
    home.Adopt_pets(cat)
    home.Adopt_pets(dog2)
    home.makeAllSounds()
    print(home.pets[0].name)
    print(home.pets[1].name)
    
if __name__ == "__main__":
    main()