class student():
    def __init__(self,name,Id,department,age,gender):
        self.name = name
        self.Id = Id
        self.department = department
        self.age = age
        self.gender = gender



obj1 = student("John", "12345", "DIT", 20, "Male")
obj2 = student("Alpha","2345","BSEM",23,"Male")
obj3 = student("Isata","3456","BBIT",44,"Female")

print(f"The info of the student is: {obj1.name},{obj1.Id}, {obj1.department},{obj1.age},{obj1.gender}")
print(f"The info of the student is: {obj2.name},{obj2.Id}, {obj2.department},{obj2.age},{obj2.gender}")
print(f"The info of the student is: {obj3.name},{obj3.Id}, {obj3.department},{obj3.age},{obj3.gender}")

