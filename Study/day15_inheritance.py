class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
   def bark(self):
       print("A Dog is barking")


class Cat(Animal):
    def meow(self):
        print("A Cat is meowing")


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.meow()