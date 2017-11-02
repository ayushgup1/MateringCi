class Animal:
    def eat(self):
      print ('1.base class')
class Dog(Animal):
   def bark(self):
      print ('2.derived class 1')
class BabyDog(Dog):
    def weep(self):
        print ('3.derived class 2')
d=BabyDog()
d.eat()
d.bark()
d.weep()