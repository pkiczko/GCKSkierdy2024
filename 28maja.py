
#z github Asabeneha 30 dni pythona

class Person:
    def __init__(self, firstname='imie', lastname = '', age = 0, kraj = "Poland", city = "Suchocin"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = kraj
        self.city = city
        self.skills = []
          

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      #def add_skill(self, skill):
      #    self.skills.append(skill)

p1 = Person("Pawel", "K", 39, 'Poland', "Warszawa")
p2 = Person()


print(p1.firstname, p1.lastname)
print(p2.firstname)

print(p1.person_info())