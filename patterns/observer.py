# Observer pattern for observing age changes
class AgeObserver:
    def update(self, person):
        print(f"Age of {person.get_name()} updated to {person.get_age()}")