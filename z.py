from pprint import pprint
class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)
    def __repr__(self):
        return "Person('%s','%s','%s')" % (self.name, self.age, self.address)

lena = Person("Лена", 19, "Пушкина, 14, 115")
oleg = Person("Олег",34,"Ленского, 10, 11")
people = {
    lena.key: lena,
    oleg.key: oleg,
}
pprint(people)
pprint(people[lena.key])
