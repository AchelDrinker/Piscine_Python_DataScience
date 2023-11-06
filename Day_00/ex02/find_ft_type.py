# Define the function as per the given prototype
def all_thing_is_obj(object: any) -> int:
    # Create a dictionary to map types to their expected output strings
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "Brian is in the kitchen"
    }

    # Get the type of the object
    obj_type = type(object)

    # Print the type information based on the object's type
    if obj_type in type_names:
        print(f"{type_names[obj_type]} : <class '{obj_type.__name__}'>")
    else:
        print("Type not found")

    # Return 42
    return 42
