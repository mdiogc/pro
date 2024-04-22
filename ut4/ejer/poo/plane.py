class Plane:
    BLACKBOX = True

    def __init__(
        self,
        fuel_capacity: float,
        max_passengers: int,
        strange_passenger: int,
        storage_capacity: float,
        manufacturer: str,
        airplane_explosion: bool,
        reactor: bool = True,
    ):
        self.fuel_capacity = fuel_capacity
        self.max_passengers = max_passengers
        self.storage_capacity = storage_capacity
        self.manufacturer = manufacturer
        self.airplane_explosion = airplane_explosion
        self.strange_passenger = strange_passenger

    def baby_crying(self):
        ADULT = 18
        for underage in self.max_passengers:
            if self.max_passengers < ADULT:
                self.max_passengers.append(underage)

    def there_is_kamikaze(self):
        if self.strange_passenger == 1:
            self.airplane_explosion = True
            pass
        else:
            msg = "This plane isn't in danger"

        print(msg)
