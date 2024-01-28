from typing import ClassVar
from numlib.utils import xgcd

# this simply jetisons metaclasses over test_zmodp2 -- no speed improvement
# and this exposes a single class
# don't subclass int
# don't coerce int, so no instance check
# use class variable

class ZModP:

    p: ClassVar[int]

    def __init__(self, value: int) -> None:
        if value < 0 or value >= ZModP.p:
            value = value % ZModP.p
        self.value = value

    def __add__(self, other: 'ZModP') -> 'ZModP':
        return ZModP(self.value + other.value)

    def __radd__(self, other: int) -> 'ZModP':
        return ZModP(other + self.value)

    def __neg__(self) -> 'ZModP':
        return ZModP(-self.value)

    def __sub__(self, other: 'ZModP') -> 'ZModP':
        return ZModP(self.value - other.value)

    def __rsub__(self, other: int) -> 'ZModP':
        return ZModP(other - self.value)

    def __mul__(self, other: 'ZModP') -> 'ZModP':
        return ZModP(self.value * other.value)

    def __rmul__(self, other: int) -> 'ZModP':
        return ZModP(self.value * other)

    def __truediv__(self, other: 'ZModP') -> 'ZModP':
        assert other.value != 0, "Cannot divide by zero."
        g, inv, _ = xgcd(other.value, ZModP.p)
        return ZModP(self.value * inv * g)

    def __rtruediv__(self, other: int) -> 'ZModP':
        assert self.value != 0, "Cannot divide by zero."
        return ZModP(other) / self

    def __pow__(self, m: int) -> 'ZModP':
        if m > 0:
            return ZModP(pow(self.value, m, ZModP.p))
        elif m < 0:
            return ZModP(1)/ZModP(pow(self.value, -m, ZModP.p))
        else:
            return ZModP(1)

    def __eq__(self, other: 'ZModP') -> bool: # type: ignore[override]
        return (self.value - other.value) % ZModP.p == 0

    #def __ne__(self, other: int|'ZModP') -> bool:
    #    return (int(self) - int(other)) % p != 0

    def __hash__(self) -> int:
        return hash((self.value))

    def __repr__(self) -> str:
        return f"{self.value} + <{ZModP.p}>"

    def __str__(self) -> str:
        return f"{self.value}"

    def isunit(self) -> bool:
        return self.value != 0

if __name__ == '__main__':
    p = 7
    F = ZModP
    F.p = p
    x = F(6)
    y = F(5)
    assert x + y == F(4)
    assert 5 + x == F(4)
    assert y - x == F(-1)
    assert 5 - x == F(-1)
    assert x * y == F(30)
    assert 3 * y == F(15)
    assert x / y == F(18)
    assert 2 / y == F(6)
    assert y ** 2 == F(4)
    assert y ** -2 == F(2)
    assert y ** 0 == F(1)

