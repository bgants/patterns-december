from patterns.factory import PersonFactory
from patterns.observer import AgeObserver


def main():
    # Factory pattern example
    factory = PersonFactory()
    person1 = factory.create_person("Alice", 25)
    person2 = factory.create_person("Bob", 30)

    # Observer pattern example
    observer = AgeObserver()
    person1.register_observer(observer)
    person2.register_observer(observer)

    # Changing age will trigger observer update
    person1.set_age(26)
    person2.set_age(31)


if __name__ == "__main__":
    main()
