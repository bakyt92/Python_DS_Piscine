import sys

def main():
    
    try:
        assert len(sys.argv) != 2, "only one argument is required"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    try:
        text = sys.argv[1]
        assert text.isalpha(), "Argument should be text"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__": 
    main()
