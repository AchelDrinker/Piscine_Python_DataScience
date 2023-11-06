import sys


def main():
    # Check that only one additional argument is provided
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        return

    # Check that the argument is an integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    # Check if the number is odd or even
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


# Run the main function
if __name__ == "__main__":
    main()
