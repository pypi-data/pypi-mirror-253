from __future__ import annotations
from typing import Iterable, Iterator, Type, cast, TYPE_CHECKING
from numlib.utils import xgcd

# this simply jetisons metaclasses over test_zmodp2 -- no speed improvement here
# and this exposes a single class
# don't subclass int
# just mod all the time

class ZModP:

    def __init__(self, p: int, value: int) -> None:
        self.value = value % p
        self.p = p

    def __add__(self, other: int|'ZModP') -> 'ZModP':
        if isinstance(other, int):
            return ZModP(self.p, self.value + int(other))
        else:
            return ZModP(self.p, self.value + other.value)

    def __radd__(self, other: int) -> 'ZModP':
        return ZModP(self.p, other + self.value)

    def __neg__(self) -> 'ZModP':
        return ZModP(self.p, -self.value)

    def __sub__(self, other: int|'ZModP') -> 'ZModP':
        if isinstance(other, int):
            return ZModP(self.p, self.value - other)
        else:
            return ZModP(self.p, self.value - other.value)

    def __rsub__(self, other: int) -> 'ZModP':
        return ZModP(self.p, other - self.value)

    def __mul__(self, other: int|'ZModP') -> 'ZModP':
        if isinstance(other, int):
            return ZModP(self.p, self.value * other)
        else:
            return ZModP(self.p, self.value * other.value)

    def __rmul__(self, other: int) -> 'ZModP':
        return ZModP(self.p, self.value * other)

    def __truediv__(self, other: int|'ZModP') -> 'ZModP':
        assert other != 0, "Cannot divide by zero."
        if isinstance(other, int):
            g, inv, _ = xgcd(other, self.p)
        else:
            g, inv, _ = xgcd(other.value, self.p)
        return ZModP(self.p, self.value * inv * g)

    def __rtruediv__(self, other: int) -> 'ZModP':
        assert self.value != 0, "Cannot divide by zero."
        if isinstance(other, int):
            return ZModP(self.p, other) / self.value
        else:
            return ZModP(self.p, other.value / self.value)

    def __pow__(self, m: int) -> None|'ZModP':
        if m > 0:
            return ZModP(self.p, pow(self.value, m, self.p))
        elif m < 0:
            return ZModP(self.p, 1)/ZModP(self.p, pow(self.value, -m, self.p))
        else:
            return ZModP(self.p, 1)

    def __eq__(self, other: int|'ZModP') -> bool: # type: ignore[override]
        if isinstance(other, int):
            return (self.value - other) % self.p == 0
        else:
            return (self.value - other.value) % self.p == 0

    #def __ne__(self, other: int|'ZModP') -> bool:
    #    return (int(self) - int(other)) % p != 0

    def __hash__(self) -> int:
        return hash((self.p, self.value))

    def __repr__(self) -> str:
        return f"{self.value} + <{self.p}>"

    def __str__(self) -> str:
        return f"{self.value}"

    def isunit(self) -> bool:
        return self.value != 0


if __name__ == '__main__':


    p = 7
    x = ZModP(p, 6)
    y = ZModP(p, 5)
    assert x + y == 4
    assert x + 5 == 4
    assert 6 + y == 4
    assert y - x == -1
    assert x - 5 == 1
    assert 5 - x == -1
    assert x * y == 30
    assert y * 3 == 15
    assert 3 * y == 15
    assert x / y == 18
    assert 2 / y == 6
    assert y / 2 == 6
    assert y ** 2 == 4
    assert y ** -2 == 2
    assert y ** 0 == 1

