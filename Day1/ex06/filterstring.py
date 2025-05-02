import sys

def main():
    try:
        assert len(sys.argv) == 3, "two arguments are required"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    text = sys.argv[1]
    dig = sys.argv[2]
    try:
        assert dig.isdigit(), "third argument should be integer"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    
if __name__ == "__main__": 
    main()