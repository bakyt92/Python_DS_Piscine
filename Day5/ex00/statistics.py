import sys
from typing import Any

class MyCustomError(Exception):
    """Exception raised for custom error scenarios.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def ft_mean(*args):
    """
    Calculate of mean value for provided list / args
    """
    total = 0
    for digit in args:
        total += digit
    return (total / len(args))


def ft_var(*args):
    """
    Calculate of Variance for provided list / args
    """
    sum_var = 0
    mean = ft_mean(*args)
    for digit in args:
        number = (digit - mean) ** 2
        sum_var += number
    return (sum_var / (len(args) - 1))

def ft_std(*args):
    variance = ft_var(*args)
    return variance ** 0.5

    
def ft_median(*args):
    lst = list(args)
    lst.sort()
    if len(lst) % 2 == 0:
        index = len(lst) // 2
        return((lst[index] + lst[index - 1]) / 2)
    else: 
        index = len(lst) // 2
        return(lst[index])


def ft_quartile(*args):
    lst = list(args)
    lst.sort()
    if len(lst) < 4:
        raise ValueError("Error: need at least 4 values for quartile")    
    if len(lst) % 4 == 0:
        q1_index = len(lst) // 4
        q3_index = len(lst) * 3 // 4
        q1 = (lst[q1_index - 1] + lst[q1_index]) / 2
        q3 = (lst[q3_index - 1] + lst[q3_index]) / 2
    else: 
        q1_index = len(lst) // 4
        q3_index = len(lst) * 3 // 4
        q1 = lst[q1_index]
        q3 = lst[q3_index]
    return q1, q3


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    operations = ["var", "std", "quartile", "mean", "median"]
    try:
        if len(args) < 2:
            raise MyCustomError("ERROR: not sufficient quantity of arguments")
        if len(kwargs) < 1:
            raise MyCustomError("ERROR: not sufficient quantity of operations")
        for digit in args:
            if not isinstance(digit, (float, int)):
                raise TypeError("ERROR: Type of data is not numeric")
        for keyword in kwargs.values():
            if keyword not in operations:
                raise NameError("ERROR: Name of transaction is not listed")
            if keyword == "std":
                print(f"STD: {ft_std(*args)}")
            elif keyword == "mean":
                print(f"mean: {ft_mean(*args)}")
            elif keyword == "var":
                print(f"var: {ft_var(*args)}")
            elif keyword == "median":
                print(f"median:  {ft_median(*args)}")
            elif keyword == "quartile":
                print(f"q1 and q3: {ft_quartile(*args)}")
    except Exception as e: 
        print(e)
        sys.exit(1)
    return

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 statistics.py 1 2 3 4 5 mean var std")
        sys.exit(1)
    operations = ["mean", "var", "std", "median", "quartile"]
    args = []
    kwargs = {}
    for token in sys.argv[1:]:
        if token in operations:
            kwargs[token] = token
        else:
            try: 
                args.append(float(token))
            except ValueError:
                print(f"ERROR: '{token}' is not a number or valid operation")
                sys.exit(1)
    ft_statistics(*args, **kwargs)
    return

if __name__ == "__main__":
    main()