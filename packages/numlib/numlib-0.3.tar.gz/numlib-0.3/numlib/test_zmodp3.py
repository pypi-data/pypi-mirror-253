from __future__ import annotations
from typing import Iterable, Iterator, Type, cast, TYPE_CHECKING
from numlib.utils import xgcd

# this simply jetisons metaclasses over test_zmodp2 -- no speed improvement here
# and this exposes a single class

class ZModP(int):
    if TYPE_CHECKING:
        p: int

    def __new__(cls: type, p: int, value: int) -> 'ZModP':
        if value < 0 or value >= p:
            value = value % p
        self: ZModP = int.__new__(cls, value)
        self.p = p
        return self

    def __add__(self, other: int|'ZModP') -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__add__(other))

    def __radd__(self, other: int) -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__radd__(other))

    def __neg__(self) -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__neg__())

    def __sub__(self, other: int|'ZModP') -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__sub__(other))

    def __rsub__(self, other: int) -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__rsub__(other))

    def __mul__(self, other: int|'ZModP') -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__mul__(other))

    def __rmul__(self, other: int) -> 'ZModP':
        return ZModP(self.p, super(ZModP, self).__rmul__(other))

    def __truediv__(self, other: int|'ZModP') -> 'ZModP':
        assert other != 0, "Cannot divide by zero."
        g, inv, _ = xgcd(int(other), self.p)
        return ZModP(self.p, super(ZModP, self).__mul__(inv * g))

    def __rtruediv__(self, other: int) -> 'ZModP': # type: ignore[misc]
        assert self != 0, "Cannot divide by zero."
        return ZModP(self.p, other).__truediv__(self)

    def __pow__(self, m: int) -> None|'ZModP': # type: ignore[override]
        if m > 0:
            return ZModP(self.p, pow(int(self), m, self.p))
        elif m < 0:
            return ZModP(self.p, 1)/ZModP(self.p, pow(int(self), -m, self.p))
        else:
            return ZModP(self.p, 1)

    def __eq__(self, other: int|'ZModP') -> bool: # type: ignore[override]
        return (int(self) - int(other)) % self.p == 0

    def __ne__(self, other: int|'ZModP') -> bool: # type: ignore[override]
        return (int(self) - int(other)) % self.p != 0

    def __hash__(self) -> int:
        return hash((int(self), self.p))

    def __repr__(self) -> str:
        return f"{super().__repr__()} + <{p}>"

    def __str__(self) -> str:
        return super().__repr__()  # for Python 3.9

    def isunit(self) -> bool:
        return self != 0


if __name__ == '__main__':


    p = 7
    x = ZModP(p, 6)
    y = ZModP(p, 6)
    print(x + y)
