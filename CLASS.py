class Animal():
    def __init__(self,name,pet,sound):
        self.name = name
        self.pet = pet
        self.sound = sound



    def speak(self):
        return f"The sound of the animal is: {self.sound}"

    def pet_info(self):
        return f"The info of the animal is: {self.name},{self.pet}, {self.sound}"


obj1 = Animal("Bigger","dog","Bark")
obj2 = Animal("Smaller","cat","Meow")

print(obj1.speak())
print(obj1.pet_info())
print(obj2.speak())
print(obj2.pet_info())