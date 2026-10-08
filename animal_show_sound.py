from abc import ABC, abstractmethod

class animal(ABC):

    def __init__ (self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(self.name, self.habitat)

    @abstractmethod
    def speak(self):
        pass
class dog(animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed
    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof Woof!")

class parrot(animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} ({self.phrase}) says: {self.phrase}! {self.phrase}!")

class lion(animal):
    def __init__(self, name, habitat, pride):
            super().__init__(name, habitat)
            self.pride = pride
    def speak(self):
            print(f"{self.name} ({self.pride}) says: ROAR! ROAR!")




dog = dog("Mac", "Home", "Golden Retriever")
parrot = parrot("Phelps", "Forest", "DOODLE!! SQAWK!")
lion = lion("Bodhi", "Savannah", "Pride Rock")

print("========== Animal Sound Show ===========\n")
for animal in [dog, parrot, lion ]:
     animal.display()
     animal.speak()
     print()