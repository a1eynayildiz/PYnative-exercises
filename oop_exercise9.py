#Check object is a subclass of a particular class


class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass
#Write a code to check the following

#Dog is a subclass of Animal? –> True
print(issubclass(Dog,Animal))
#Animal is a subclass of Dog? –> False
print(issubclass(Animal,Dog))
#Cat is a subclass of Animal? –> False
print(issubclass(Cat,Animal))
#Puppy is a subclass of Animal –> True
print(issubclass(Puppy,Animal))

