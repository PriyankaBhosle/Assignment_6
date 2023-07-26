# Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
#  d. Create objects and implement the above functionalities

class Dog:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def description(self):
        print(self.name, self.age)
    def get_info(self):
        print(" Coat colour of the dog is Black ")


p1 = Dog ("Rocky",5)
p1.description()
p1.get_info() 


#Child class
class JackRussellTerrier(Dog):
    def __init__(self,name,age,):
      Dog.__init__(self,name,age)

    def make_sound(self):
        print(" making sound of Bark")
    def gender(self):
        print("Male")


object = JackRussellTerrier("jack", 5) 
object.description()
object.get_info() 
object.make_sound()
object.gender()

class Bulldog(Dog):
    def __init__(self,name,age,):
      Dog.__init__(self,name,age)
    def make_sound(self):
        print(" making sound of Bark")
    def gender(self):
        print("Male")

Bulldog_obj = Bulldog("Tommy", 7)
Bulldog_obj.description()
Bulldog_obj.get_info()
Bulldog_obj.make_sound()
Bulldog_obj.gender





