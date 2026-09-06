import sys


def square(x: int | float) -> int | float:
    if not isinstance(x, (float, int)):
        raise ValueError("Input data is not float / int")
    res = x * x
    return res


def pow(x: int | float) -> int | float:
    if not isinstance(x, (float, int)):
        raise ValueError("Input data is not float / int")
    return x ** x


def outer(x: int | float, function) -> object:
    if not isinstance(x, (float, int)):
        raise ValueError("Input data is not float / int")
    count = 0

    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    return inner


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Error, no sufficient args")
        functions = {
                "square": square,
                "pow": pow,
            }
        if sys.argv[1] == "outer":
            if len(sys.argv) != 4:
                raise ValueError("Error, no sufficient args")
            func_name = sys.argv[3]
            value = float(sys.argv[2])
            counter = outer(value, functions[func_name])
            res = counter()
        else:
            if len(sys.argv) != 3:
                raise ValueError("Error, no sufficient args")
            if sys.argv[1] not in functions:
                raise ValueError("Error, this function is not allowed. "
                                 "Try python3 in_out.py pow 3")
            func_name = sys.argv[1]
            value = float(sys.argv[2])
            res = functions[func_name](value)
        print(f"Result is: {res}")
    except ValueError as e:
        print(e)
        return 1
    return 0


if __name__ == "__main__":
    main()
