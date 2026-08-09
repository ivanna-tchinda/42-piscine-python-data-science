from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""

    def __init__(
        self,
        first_name,
        is_alive=True,
        family_name="Baratheon",
        eyes="brown",
        hair="dark"
    ):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hair = hair

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hair):
        self.hair = hair

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hair