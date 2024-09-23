#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Exponentiation:

    def __init__(self, first=0.0, second=0.0):
        first = float(first)
        second = float(second)

        self.__number = first
        self.__exponent = second

        if first < 0:
            raise ValueError
        
    # Клонировать выражение
    def __clone(self):
        return Exponentiation(self.__number, self.__exponent)
        
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        if value >= 0:
            self.__number = float(value)
        else:
            raise ValueError("Illegal value")

    @property
    def exponent(self):
        return self.__exponent    
    
    @exponent.setter
    def exponent(self, value):
        self.__exponent = float(value)

    def power(self):
        return self.number**self.exponent

    # Привести выражение к строке
    def __str__(self):
        return f"{self.__number}^{self.__exponent}"

    def __repr__(self) -> str:
        return self.__str__()
    
    # Привести выражение к логическому значению.
    def __bool__(self):
        return self.__number != 0
    
    # перемножение степеней с одинаковыми основаниями
    def __imul__(self, rhs): # *=
        if isinstance(rhs, Exponentiation):
            a = self.exponent + rhs.exponent

            self.__exponent = a
            return self
        else:
            raise ValueError("Illegal type of the argument")
        
    def __mul__(self, rhs): # *
        return self.__clone().__imul__(rhs)
        
    # деление степеней с одинаковыми основаниями
    def __itruediv__(self, rhs): # /=
        if isinstance(rhs, Exponentiation):
            a = self.exponent - rhs.exponent

            self.__exponent = a
            return self
        else:
            raise ValueError("Illegal type of the argument")
        
    def __truediv__(self, rhs): # /
        return self.__clone().__itruediv__(rhs)
    
    def __eq__(self, rhs):  # ==
        if isinstance(rhs, Exponentiation):
            return self.power() == rhs.power()
        else:
            return False

    def __ne__(self, rhs):  # !=
        if isinstance(rhs, Exponentiation):
            return not self.__eq__(rhs)
        else:
            return False

    def __gt__(self, rhs):  # >
        if isinstance(rhs, Exponentiation):
            return self.power() > rhs.power()
        else:
            return False

    def __lt__(self, rhs):  # <
        if isinstance(rhs, Exponentiation):
            return self.power() < rhs.power()
        else:
            return False

    def __ge__(self, rhs):  # >=
        if isinstance(rhs, Exponentiation):
            return not self.__lt__(rhs)
        else:
            return False

    def __le__(self, rhs):  # <=
        if isinstance(rhs, Exponentiation):
            return not self.__gt__(rhs)
        else:
            return False
        
if __name__ == '__main__':
    e1 = Exponentiation(0.5, 0.2)
    print(f"e1 = {e1}")

    e2 = Exponentiation(0.5, 1.3)
    print(f"e2 = {e2}")

    print(f"e1 * e2 = {e1 * e2}")
    print(f"e1 / e2 = {e1 / e2}")

    
    print(f"e1 == e2: {e1 == e2}")
    print(f"e1 != e2: {e1 != e2}")
    print(f"e1 > e2: {e1 > e2}")
    print(f"e1 < e2: {e1 < e2}")
    print(f"e1 >= e2: {e1 >= e2}")
    print(f"e1 <= e2: {e1 <= e2}")