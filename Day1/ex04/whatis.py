import sys

try:
    assert len(sys.argv) < 3, "AssertionError: more than one argument is provided"
    assert len(sys.argv) > 1, "AssertionError: please provide an integer argument"
    x = sys.argv[1]
    assert x.isdigit(), "AssertionError: argument is not an integer"
except AssertionError as error:
    print(error)
    sys.exit(1)

var = int(sys.argv[1])
if var%2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")