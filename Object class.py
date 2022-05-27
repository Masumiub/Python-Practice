class partyanimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = partyanimal("Sally")
s.party()

j = partyanimal("Jim")
j.party()
s.party()

#class - a template
#Attribute - a variable within a class
#method- a function within a class
#object - a particular instance of a .class
#constructor - code that runs when an object is created.
#inheritance - the ability to extend a class to make a new class 
