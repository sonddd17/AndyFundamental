class Animal:
    def __init__(self, name):
        self.name =  name
    def speak(self):
        print(self.name, "make a sound")

class Dog(Animal):
    def speak(self):
        print(self.name,  "barks")

myAnimal = Animal("Tun")

myAnimal.speak()

Dog("Rex").speak()