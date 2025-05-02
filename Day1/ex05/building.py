import sys
import string

def analyze_text(string1):
    digits = 0
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0

    for i in string1:
        if i.isdigit():
            digits += 1
        elif i.isspace():
            spaces += 1
        elif i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i in string.punctuation:
            punctuation += 1
    print("The text cointains ", len(string1), "characters")
    print(upper, " upper letters")
    print(lower, " lower letters")
    print(punctuation, " punctuation marks")
    print(spaces, " spaces")
    print(digits, " digits")

def main(): 
    # your tests and your error handling 
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        sys.exit(1)
    if len(sys.argv) == 1:
        try: 
            string1 = input("What is the text to count?\n")
            string1 += "\n"
        except EOFError:
            pass
    else:
        string1 = sys.argv[1]    
    analyze_text(string1)
    

if __name__ == "__main__": 
    main()

# For tests
# "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
# from chatgpt - Here is the accurate count for the text you provided:
# Total Characters: 170
# Letters: 123
# Digits: 15
# Punctuation Marks: 7
# Whitespaces: 25

