class Person:
    def __innit__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
       print(self.firstname, self.lastname)


class student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

x = student("Joey", "king", 2021)
x.printname()
print(x.graduationyear)