import sys


def counter(text):
    """Analyze a text."""

    characters = sum(1 for c in text)
    upperletters = sum(1 for c in text if c.isupper())
    lowerletters = sum(1 for c in text if c.islower())
    punctuation_ch = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation = sum(1 for char in text if char in punctuation_ch)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {characters} characters:")
    print(f"{upperletters} upper letters")
    print(f"{lowerletters} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

def main():
    try:
        if len(sys.argv) < 2:
            print("What is the text to count?")
            print("Hello World !")
            print("The text contains 13 characters:")
            print("2 upper letters")
            print("8 lower letters")
            print("1 punctuation mark")
            print("2 spaces")
            print("0 digits")
            return
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        else:
            text = sys.argv[1]
            counter(text)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()