import sys
from ft_filter import ft_filter


def filter_string(S, N):
    """Filter a string by length"""

    is_longer_than_N = lambda word: len(word) > N
    word_list = [word for word in S.split(' ') if is_longer_than_N(word)]
    return list(word_list)

def check_string(S):
    """Check if the string is valid"""
    if not isinstance(S, str):
        raise AssertionError("AssertionError: the arguments are bad")

    if len(S) == 0:
        raise AssertionError("AssertionError: the arguments are bad")

    if not all(char.isalpha() or char.isspace() for char in S):
        raise AssertionError("AssertionError: the arguments are bad")
    return True


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        S = sys.argv[1]
        check_string(S)
        N = int(sys.argv[2])
    except (AssertionError, ValueError):
        raise AssertionError("AssertionError: the arguments are bad") from None
    
    
    word_list = filter_string(S, N)
    print(list(word_list))

if __name__ == "__main__":
    main()
