from S1E9 import Character


class Baratheon(Character):
    """ Representing Baratheon Family """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Creates Barathen Family Character, subclass of Character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "Brown"
        self.hairs = "Dark"
        return

    def __str__(self):
        """Return __str__ (short description for users)"""
        return f'Vector ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        """Return __str__ (detailes description for developers)"""
        return f'Vector ({self.family_name}, {self.eyes}, {self.hairs})'

    def die(self):
        """Kill the Character by setting is_alive to False."""
        self.is_alive = False
        return


class Lannister(Character):
    """ Representing Lannister Family """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Creates Lannister Family Character, subclass of Character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "Blue"
        self.hairs = "Light"
        return

    def __str__(self):
        """Return __str__ (short description for users)"""
        return f'Vector ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        """Return __str__ (detailes description for developers)"""
        return f'Vector ({self.family_name}, {self.eyes}, {self.hairs})'

    def die(self):
        """Kill the Character by setting is_alive to False."""
        self.is_alive = False
        return

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create Lannister family member"""
        return cls(first_name, is_alive)
