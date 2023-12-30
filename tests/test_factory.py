from patterns import factory


def test_factory():
    assert factory.PersonFactory().create_person("John", 42).name == "John"
