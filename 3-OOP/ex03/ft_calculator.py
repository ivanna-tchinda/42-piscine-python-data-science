class calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return calculator([x + other for x in self.value])

    def __sub__(self, other):
        return calculator([x - other for x in self.value])

    def __mul__(self, other):
        return calculator([x * other for x in self.value])

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return calculator([x / other for x in self.value])

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)