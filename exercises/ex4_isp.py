"""
Exercise 4 - Interface Segregation Principle (ISP)

VehicleActions below is a single "fat" interface that forces every
vehicle to implement actions that make no sense for it: a GasCar has no
pedals, a Bicycle has no engine or wings, and neither can fly. Both are
forced to implement fly() (and other irrelevant methods) with an
"I can't do that" stub -- a classic ISP violation.

YOUR TASK:
  1. Replace the one fat `VehicleActions` interface with several small,
     focused ones: `Movable` (move), `Refuelable` (refuel), `Flyable`
     (fly), `Pedalable` (pedal_harder) -- each with exactly ONE abstract
     method.
  2. Make GasCar implement only Movable + Refuelable, and Bicycle only
     Movable + Pedalable. Remove their now-unnecessary
     NotImplementedError stubs entirely.
  3. Add a new `Drone` class that implements Movable + Flyable (move()
     and fly()) -- and nothing else. It should NOT be forced to
     implement refuel() or pedal_harder().

Run it to see the race once Drone exists:
    python -m exercises.ex4_isp

Check your work:
    pytest tests/test_ex4_isp.py -v
"""
from abc import ABC, abstractmethod

from engine.track import Track

class Movable(ABC):
    @abstractmethod
    def move(self) -> None: ...

class Refuelable(ABC):
    @abstractmethod
    def refuel(self) -> None: ...

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None: ...

class Pedalable(ABC):
    @abstractmethod
    def pedal_harder(self) -> None: ...


# TODO(ISP): define Movable, Refuelable, Flyable and Pedalable here,
# each with exactly one abstract method, and delete VehicleActions above
# once nothing uses it any more.


class GasCar(Movable, Refuelable):
    symbol = "\U0001F697"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 5

    def refuel(self):
        print(f"{self.name} refuels at the gas station.")


class Bicycle(Movable, Pedalable):
    symbol = "\U0001F6B2"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3

    def pedal_harder(self):
        self.position += 1
        print(f"{self.name}'s rider pedals harder!")


# TODO(ISP): add a Drone class here (Movable + Flyable only).
class Drone(Movable, Flyable):
    symbol = "\U00002708"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 4

    def fly(self):
        print(f"{self.name} can fly")


# TODO(ISP): add a Drone class here (Movable + Flyable only).


def main():
    vehicles = [GasCar("Racer"), Bicycle("Pedal Pete"), Drone("Sky Scout")]
    # TODO(ISP): once Drone exists, add Drone("Sky Scout") to the race.
    Track(length=50).run(vehicles)


if __name__ == "__main__":
    main()
