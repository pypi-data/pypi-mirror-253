from numlib.utils import xgcd

# this simply jetisons metaclasses over test_zmodp2 -- no speed improvement here
# and this exposes a single class
# don't subclass int
# don't coerce int, so no instance check

class ZModP:

    def __init__(self, p: int, value: int) -> None:
        if value < 0 or value >= p:
            value = value % p
        self.value = value
        self.p = p

    def __add__(self, other: 'ZModP') -> 'ZModP':
        return ZModP(self.p, self.value + other.value)

    def __radd__(self, other: int) -> 'ZModP':
        return ZModP(self.p, other + self.value)

    def __neg__(self) -> 'ZModP':
        return ZModP(self.p, -self.value)

    def __sub__(self, other: 'ZModP') -> 'ZModP':
        return ZModP(self.p, self.value - other.value)

    def __rsub__(self, other: int) -> 'ZModP':
        return ZModP(self.p, other - self.value)

    def __mul__(self, other: 'ZModP') -> 'ZModP':
        return ZModP(self.p, self.value * other.value)

    def __rmul__(self, other: int) -> 'ZModP':
        return ZModP(self.p, self.value * other)

    def __truediv__(self, other: 'ZModP') -> 'ZModP':
        assert other.value != 0, "Cannot divide by zero."
        g, inv, _ = xgcd(other.value, self.p)
        return ZModP(self.p, self.value * inv * g)

    def __rtruediv__(self, other: int) -> 'ZModP':
        assert self.value != 0, "Cannot divide by zero."
        return ZModP(self.p, other) / self

    def __pow__(self, m: int) -> 'ZModP':
        if m > 0:
            return ZModP(self.p, pow(self.value, m, self.p))
        elif m < 0:
            return ZModP(self.p, 1)/ZModP(self.p, pow(self.value, -m, self.p))
        else:
            return ZModP(self.p, 1)

    def __eq__(self, other: 'ZModP') -> bool: # type: ignore[override]
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
    assert x + y == ZModP(p, 4)
    assert 5 + x == ZModP(p, 4)
    #assert x + 5 == ZModP(p, 4)
    assert y - x == ZModP(p, -1)
    assert 5 - x == ZModP(p, -1)
    #assert x - 5 == ZModP(p, -1)
    assert x * y == ZModP(p, 30)
    assert 3 * y == ZModP(p, 15)
    #assert y * 3 == ZModP(p, 15)
    assert x / y == ZModP(p, 18)
    assert 2 / y == ZModP(p, 6)
    #assert y / 2 == ZModP(p, 6)
    assert y ** 2 == ZModP(p, 4)
    assert y ** -2 == ZModP(p, 2)
    assert y ** 0 == ZModP(p, 1)

