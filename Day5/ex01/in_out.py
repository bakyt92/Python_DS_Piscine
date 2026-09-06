import sys


def square(x: int | float) -> int | float:
    return


def pow(x: int | float) -> int | float:
    return


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        return


def main():
    if len(sys.argv) < 3:
        raise ValueError("Error, no sufficient args")
    functions = {
        "outer": outer,
        "square": square,
        "pow": pow,
    }
    if sys.argv[2] not in functions:
        raise ValueError("Error, this function is not allowed")
    func_name = sys.argv[2]
    try:
        value = float(sys.argv[1])
        res = functions[func_name](value)
        print(f"Result is: {res}")
    except ValueError:
        raise ValueError("First argument should be integer / float")
    return


if __name__ == "__main__":
    main()
