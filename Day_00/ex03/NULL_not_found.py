import math


def NULL_not_found(object: any) -> int:
    # Check for NoneType or NaN
    if object is None:
        print(f"Nothing : {object} <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese : {object} <class 'float'>")
        return 0

    # Check for 0, empty string, and False
    if object == 0:
        print(f"Zero : {object} <class 'int'>")
        return 0
    elif object == '':
        print("Empty : <class 'str'>")
        return 0
    elif object is False:
        print(f"Fake : {object} <class 'bool'>")
        return 0

    # If the object is not a recognized null type,
    # print an error message and return 1
    print("Type not Found")
    return 1
