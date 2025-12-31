def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI

    Args: 2 lists of floats or ints (height and weight)

    Return: list of calculated BMI 
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Wrong type, it should be a list")
        if len(height) != len(weight):
            raise ValueError("It should be equal number of elements")
    except Exception as error:
        print("You have following error: ", error)
        return []
    try:
        result = []
        for h, w in zip(height, weight):
            if (not isinstance(h, (float, int)) or
                    not isinstance(w, (float, int))):
                raise TypeError("Wrong type, it should be a int / float")
            values = w / (h ** 2)
            result.append(values)
    except Exception as error:
        print("You have following error: ", error)
        return []
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies limit and responds with list of True / False
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("Wrong type, it should be a list")
        result = []
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise TypeError("Wrong type, it should be a int / float")
            if b > limit:
                value = True
            else:
                value = False
            result.append(value)
    except Exception as error:
        print("You have following error: ", error)
        return []
    return result


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    # test wrong data
    # height = [2.71, 'a', 1.15]
    # weight = [165.3, 38.4]

    result = give_bmi(height, weight)
    if result:
        print(result)
    limits = apply_limit(result, 22)
    if limits:
        print(limits)
    return


if __name__ == "__main__":
    main()
