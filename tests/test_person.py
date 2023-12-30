from models.person import Person


def test_create_person():
    person = Person("Bob", 56)
    assert person.name == "Bob"
    assert person.age == 56
