# Person class representing the data model
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._observers = []  # List to store observers for Observer pattern

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        self.notify_observers()  # Notify observers when age is updated

    # Observer pattern methods
    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)
