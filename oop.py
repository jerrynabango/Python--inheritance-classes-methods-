class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Jambo, my name is {self.name}. I'm {self.age} years old and identify as {self.gender}.")


person = Person("Jerry Nabango", 17, "Male")

person.introduce()
