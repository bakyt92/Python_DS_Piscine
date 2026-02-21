import sys

class calculator:
    """ Calculator instance"""

    def __init__(self, _data):
        """ Creates Character """
        try: 
            for x in _data: 
                if isinstance(x, (int, float)):
                    continue
                else:
                    ValueError("Input data are not numbers: int or floats")
        except Exception as e:
            print(e)
            sys.exit(1)
        self.data = list(_data)
        return
    
    def __add__(self, object) -> None:
        """Function performs addition to vector with a scalar"""
        try:
            if not isinstance(object, (int, float)):
                ValueError("Input data are not numbers: int or floats")
            list1 = self.data
            for i, val in enumerate(list1):
                list1[i] = val + object
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return

    def __mul__(self, object) -> None:
        """Function performs multiplication to vector with a scalar"""
        try:
            if not isinstance(object, (int, float)):
                ValueError("Input data are not numbers: int or floats")
            list1 = self.data
            for i, val in enumerate(list1):
                list1[i] = val * object
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return


    def __sub__(self, object) -> None:
        """Function performs multiplication to vector with a scalar"""
        try:
            if not isinstance(object, (int, float)):
                ValueError("Input data are not numbers: int or floats")
            list1 = self.data
            for i, val in enumerate(list1):
                list1[i] = val - object
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return


    def __truediv__(self, object) -> None:
        """Function performs multiplication to vector with a scalar"""
        try:
            if not isinstance(object, (int, float)):
                ValueError("Input data are not numbers: int or floats")
            assert object != 0, "Division by zero, Error"
            list1 = self.data
            for i, val in enumerate(list1):
                list1[i] = val / object
            self.data = list1
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Res is: {self.data}')
        return