"""
Exercise 3 - Liskov Substitution Principle (LSP)

Every Vehicle in this module must honor the same contract (see Track's
own docstring/engine.track.Racer): move() always leaves position >= its
previous value, and move() never raises. Track relies on this contract
to run any race safely -- anything that can't honor it should not be a
Vehicle.

UnreliableCar below breaks that contract on purpose: run it a few times
and watch it either crash the race or roll backwards.

YOUR TASK: redesign UnreliableCar's move() so "being unreliable" no
longer violates the contract. Model unreliability as something the
contract allows -- for example, some ticks it simply does not advance
(stays exactly where it is) -- instead of raising or moving backwards.
Do not change the Vehicle base class or Track.

Run it to see the current (broken) behavior:
    python -m exercises.ex3_lsp

Check your work:
    pytest tests/test_ex3_lsp.py -v
"""
import random

from engine.track import Track


class Vehicle:
    """Contract every vehicle here must honor:
    - move() must leave position >= its previous value (never backwards).
    - move() must never raise.
    Any subclass that cannot honor this contract must not be a Vehicle.
    """

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class SteadyCar(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class UnreliableCar(Vehicle):
    """VIOLATION (on purpose): sometimes this 'car' rolls backward or
    blows up mid-race, breaking every caller that assumed a Vehicle only
    ever moves forward and never raises. Fix move() below.
    """

    symbol = "\U0001F699"

    def move(self) -> None:
        # TODO(LSP): rewrite this so it never raises and never decreases
        # `self.position`. "Unreliable" can still mean something (e.g.
        # occasionally staying in place) -- it just can't break the
        # Vehicle contract.
        roll = random.random()
        if roll < 0.3:
            return # doesn't move
        self.position += 5


def main():
    vehicles = [SteadyCar("Reliable Rex"), UnreliableCar("Shaky Sam")]
    Track(length=50).run(vehicles)  # <-- may crash or derail until you fix it


if __name__ == "__main__":
    main()
