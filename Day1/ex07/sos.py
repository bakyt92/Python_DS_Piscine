import sys

NESTED_MORSE = { " ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "0": "----- ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. "}

def main():
    
    try:
        assert len(sys.argv) == 2, "only one argument is required"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return
    try:
        text = sys.argv[1]
        text = text.upper()
        nospaces_text = text.replace(" ", "")
        assert nospaces_text.isalnum(), "Argument should be text"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return
    for x in text:
        symbol = NESTED_MORSE.get(x)
        if symbol:
            print(symbol, end="")
    print()
    return


if __name__ == "__main__": 
    main()
