import sys


class calculator:
    """ Calculator instance"""

    def __init__(self, _data):
        """ Creates Calculator instance """
        try:
            self.data = list(_data)
            for x in self.data:
                if isinstance(x, (int, float)):
                    continue
                else:
                    raise ValueError("Input data are not numbers: int or floats")
        except Exception as e:
            print(e)
            sys.exit(1)
        return

    def __add__(self, scalar) -> None:
        """Function performs addition to vector with a scalar"""
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Input data are not numbers: int or floats")
            list1 = list(self.data)
            for i, val in enumerate(list1):
                list1[i] = val + scalar
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return

    def __mul__(self, scalar) -> None:
        """Function performs multiplication to vector with a scalar"""
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Input data are not numbers: int or floats")
            list1 = list(self.data)
            for i, val in enumerate(list1):
                list1[i] = val * scalar
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return

    def __sub__(self, scalar) -> None:
        """Function performs multiplication to vector with a scalar"""
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Input data are not numbers: int or floats")
            list1 = list(self.data)
            for i, val in enumerate(list1):
                list1[i] = val - scalar
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return

    def __truediv__(self, scalar) -> None:
        """Function performs multiplication to vector with a scalar"""
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Input data are not numbers: int or floats")
            assert scalar != 0, "Division by zero, Error"
            list1 = list(self.data)
            for i, val in enumerate(list1):
                list1[i] = val / scalar
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return
