"""
Practical Use Classes (puc)
"""

class C:
    """A single 2D Coordinate"""

    def __init__(self, x, y):
        if not isinstance(x, (int, float)):
            raise TypeError("x only accepts an int or a float")
        self.x = x
        if not isinstance(y, (int, float)):
            raise TypeError("y only accepts an int or a float")
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, C):
            return self.x == other.x and self.y == other.y


class NeoStr(str):
    """Daughter class of string because I want custom string methods."""

    def index_all(self, char) -> list:
        """Returns a list of indexes for every occurrence of Char in self."""
        last_ind = 0
        string_ind = []
        for x in range(self.count(char)):
            string_ind.append(self.index(char, last_ind))
            last_ind = self.index(char, last_ind) + 1
        return string_ind

    def isfloatable(self):
        """Like .isdigit() but also looks for '.'"""
        return True if self.replace(".", "").isdigit() and self.count(".") <= 1 else False

#    def lispify(self):
#        """For practical use, of course...
#        Replaces every s in self with th."""
#        return self.replace("s", "th")


class NeoInt(int):
    """Daughter class of integer because I want custom integer methods."""

    def iseven(self) -> bool:
        return True if self % 2 == 0 else False

    def isprime(self) -> bool:
        if self <= 1:
            return False
        if self == 2:
            return True
        for index in range(2, self - 1):
            if self % index == 0:
                return False
        return True

    
class NeoList(list):
    pass


class Date:  # This was the most useful thing I'd ever coded until I discovered datetime, making Date obselete. Fuck.
    """Class with 3 int attributes: a year, a month, and a day."""

    def __init__(self, year, month, day):
        if not isinstance(year, int):
            raise TypeError("year must be set to an int")
        self.year = year

        if not isinstance(month, int):
            raise TypeError("month must be set to an int")
        if month > 12 or month < 1:
            raise ValueError("month must be in range 1-12")
        self.month = month

        if not isinstance(day, int):
            raise TypeError("day must be set to an int")
        if month == 2:
            if year % 4 == 0:
                last_day = 29
            else:
                last_day = 28
        elif month == (4 or 6 or 9 or 11):
            last_day = 30
        else:
            last_day = 31
        if day > last_day or day < 1:
            raise ValueError("current value of day is impossible")
        self.day = day
    
    def __str__(self):
        """
        a Date's default appearance in console is day/month/year.
        However, use .display() method to return a string in whatever order you'd like.
        """
        return str(self.day)+"/"+str(self.month)+"/"+str(self.year)

    def __repr__(self):
        return f"(year={str(self.year)} month={str(self.month)} day={str(self.day)})"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.year == other.year and self.month == other.month and self.day == other.day

    @classmethod
    def random(cls, start=1900, end=2020):
        """Generates a random instance of Date within range start to end (defaults to 1900-2020)"""
        from random import randint, seed
        seed()
        year = randint(start, end)
        month = randint(1, 12)
        if month == 2:
            if year % 4 == 0:
                last_day = 29
            else:
                last_day = 28
        elif month == (4 or 6 or 9 or 11):
            last_day = 30
        else:
            last_day = 31
        day = randint(1, last_day)
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Uses Date and time.localtime() to return today's date as an instance of Date"""
        from time import localtime
        return cls(localtime()[0], localtime()[1], localtime()[2])

    @classmethod
    def yday(cls):
        """Uses Date and time.localtime() to return yesterday's date as an instance of Date"""
        from time import localtime
        return cls(localtime()[0], localtime()[1], localtime()[2] - 1)

    @classmethod
    def tmw(cls):
        """Uses Date and time.localtime() to return tomorrow's date as an instance of Date"""
        from time import localtime
        return cls(localtime()[0], localtime()[1], localtime()[2] + 1)

    def display(self, order="dmy") -> str:
        """
        Returns str(self) in a customizable order using the order parameter.
        To use the order parameter, simply pass in a string with 3 chars: y, m, d.
        The order of these 3 chars will determine the return's order.
        (ex: Date(2001, 3, 9).display("mdy") -> "3/9/2001")
        """
        if len(order) != 3:
            raise RuntimeError('"' + order + '" must be 3 characters long exactly')
        abbr = {"y": str(self.year), "m": str(self.month), "d": str(self.day)}
        return abbr[order[0]] + "/" + abbr[order[1]] + "/" + abbr[order[2]]

    def age_get(self) -> int:
        """will return an int of how old someone born on self is at the time of calling age_get."""
        from time import localtime
        crnt_year, crnt_month, crnt_day = localtime()[0], localtime()[1], localtime()[2]

        years_passed = (crnt_year - 1) - self.year
        if crnt_month < self.month:
            return years_passed
        if crnt_month > self.month:
            return years_passed + 1
        if crnt_month == self.month:
            if crnt_day >= self.day:
                return years_passed + 1
            else:
                return years_passed
            

class Person:

    def __init__(self):
        pass

