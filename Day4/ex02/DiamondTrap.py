from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ Representing KING class """
    def __init__(self, first_name: str, is_alive: bool = True):
        """ Creates STARK Character, subclass of Character """
        super().__init__(first_name, is_alive)
        return

    @property
    def eyes(self):
        """Returns colour of eyes"""
        return self.__dict__["eyes"]

    @property
    def hairs(self):
        """Returns colour of hairs"""
        return self.__dict__["hairs"]

    @eyes.setter
    def eyes(self, value):
        """Setter method - property for eyes"""
        self.__dict__["eyes"] = value

    @hairs.setter
    def hairs(self, value: str):
        """Setter method - property for hairs"""
        self.__dict__["hairs"] = value

    def set_eyes(self, _eyes: str):
        """ Set method to set color of eyes """
        self.eyes = _eyes

    def set_hairs(self, _hairs: str):
        """ Set method to set color of eyes """
        self.hairs = _hairs

    def get_hairs(self):
        """ Getter method for hairs """
        return (self.hairs)

    def get_eyes(self):
        """ Getter method for eyes """
        return (self.eyes)

    def die(self):
        """Abstract (mandatory method for
        all character class instances)
        Sets value is_alive to False"""
        super().die()
        return
