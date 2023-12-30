# Factory pattern for creating Person objects
from models.person import Person


class PersonFactory:
    def create_person(self, name, age):
        return Person(name, age)