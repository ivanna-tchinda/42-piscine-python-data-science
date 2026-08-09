from S1E9 import Character


class Baratheon(Character):
    """Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        return f"Name : ({self.first_name}, 'Baratheon'), Alive : {self.is_alive}"

    def __repr__(self):
        return f"Name : ({self.first_name}, 'Baratheon'), Alive : {self.is_alive}"

    def die(self):
        self.is_alive = False


class Lannister(Character):
    """Lannister family"""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        return f"Name : ({self.first_name}, 'Lannister'), Alive : {self.is_alive}"

    def __repr__(self):
        return f"Name : ({self.first_name}, 'Lannister'), Alive : {self.is_alive}"

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)