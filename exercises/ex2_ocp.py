"""
Exercise 2 - Open/Closed Principle (OCP)

Vehicle, Car and Truck below are COMPLETE and WORKING -- treat them as
"closed for modification". Do not change them (or Track).

YOUR TASK: implement Motorcycle and Bicycle purely by EXTENSION (new
subclasses of Vehicle), so the race in main() ends up showing four very
different movement patterns:

  - Motorcycle: fast but erratic -- its step size should vary a lot from
    tick to tick (e.g. sometimes a small wobble, sometimes a big burst).
  - Bicycle: starts strong but gets slower over time as the rider tires
    out (its step size should shrink, but never drop below 1).

If finishing this exercise ever makes you want to edit Vehicle, Car,
Truck or Track, that's a sign your design isn't using OCP yet --
polymorphism (new subclasses) should be enough.

Run it to watch the race:
    python -m exercises.ex2_ocp

Check your work:
    pytest tests/test_ex2_ocp.py -v
"""

from engine.track import Track
import random


class Vehicle:
    """Base type every racer in this exercise extends."""

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class Car(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class Truck(Vehicle):
    symbol = "\U0001F69A"

    def move(self) -> None:
        self.position += 2


class Motorcycle(Vehicle):
    symbol = "\U0001F3CD"

    def move(self) -> None:
        # TODO(OCP): move forward by a varying, sometimes-large amount.
        self.position += random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class Bicycle(Vehicle):
    symbol = "\U0001F6B2"

    def __init__(self, name: str):
        super().__init__(name)
        # TODO(OCP): add any state you need to track fatigue over time.
        self._ticks = 0

    def move(self) -> None:
        # TODO(OCP): move forward by a shrinking amount as ticks go by
        # (never less than 1).
        self._ticks+=1
        self.position += max(1, 6-self._ticks//2)


def main():
    vehicles = [
        Car("Red Car"),
        Truck("Big Rig"),
        Motorcycle("Ghost Rider"),
        Bicycle("Pedal Pete"),
    ]
    Track(length=100).run(vehicles)


if __name__ == "__main__":
    main()
