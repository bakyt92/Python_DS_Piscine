import numpy as numpy


def slice_me(family: list, start: int, end: int) -> list:
    """
        Function returns truncated version of input Array
        Args: array
        Return: list of truncated version
    """
    try:
        assert isinstance(family, list), "Variable family is not a list"
        assert isinstance(start, int), "Variable start is not a int"
        assert isinstance(end, int), "Variable start is not a int"
    except AssertionError as error:
        print(f"Error raised: {error}")
        return []
    print("My shape is:", numpy.array(family).shape)
    new_list = list(family[start:end])
    print("My new shape is:", numpy.array(new_list).shape)
    return new_list


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
