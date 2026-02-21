from abc import ABC, abstractmethod


class Character(ABC):
    """Class of main character in this application"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """ Creates Character """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract (mandatory method for
        all character class instances)
        Sets value is alive to False"""
        self.is_alive = False
        return


class Stark(Character):
    """ Representing Stark Family """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Creates STARK Character, subclass of Character """
        super().__init__(first_name, is_alive)
        return

    def die(self):
        """Kill the Stark by setting is_alive to False."""
        self.is_alive = False
        return
