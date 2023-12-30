from patterns import factory
from patterns.observer import AgeObserver


def test_observer(capfd):
    john = factory.PersonFactory().create_person("John", 42)
    observer = AgeObserver()
    john.register_observer(observer)
    john.set_age(43)
    captured = capfd.readouterr()
    assert captured.out.strip() == "Age of John updated to 43"
