import sys


class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculation of dot product of 2 vectors"""
        try:
            assert len(V1) == len(V2), "Non-equal number of elements"
            temp = 0
            res = 0
            for i, x in enumerate(V1):
                temp = x * V2[i]
                res += temp
        except Exception as e:
            print(e)
            sys.exit(1)
        print(f'Dot product is: {res}')
        return

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculation of sum of 2 vectors"""
        try:
            assert len(V1) == len(V2), "Non-equal number of elements"
            list1 = []
            for i, x in enumerate(V1):
                list1.append(x + V2[i])
        except Exception as e:
            print(e)
            sys.exit(1)
        formatted = [f"{x: .2f}" for x in list1]
        print(f'Add vector is {formatted}')
        return

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculation of sous of 2 vectors"""
        try:
            assert len(V1) == len(V2), "Non-equal number of elements"
            list1 = []
            for i, x in enumerate(V1):
                list1.append(x - V2[i])
        except Exception as e:
            print(e)
            sys.exit(1)
        formatted = [f"{x: .2f}" for x in list1]
        print(f'Sous vector is {formatted}')
        return
