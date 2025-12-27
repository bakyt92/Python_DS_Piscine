import sys

def main():
    try:
        assert len(sys.argv) == 3, "two arguments are required"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    text = sys.argv[1]
    dig = int(sys.argv[2])
    try:
        dig = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return
    text_list = text.split()
    text_output = [x for x in text_list if (lambda w: len(w) >= dig)(x)]
    print(text_output)
    return

if __name__ == "__main__": 
    main()