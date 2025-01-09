def is_nan(value):
    return value != value


def NULL_not_found(object: any) -> int:
    typeee = type(object)
    name = ""
    if object is None:
        name = "Nothing"
    elif is_nan(object):
        name = "Cheese"
        print(f"{name}: {object} {typeee}")
        return 0
    elif typeee.__name__ == "int" and object == 0:
        name = "Zero"
    elif object == "":
        name = "Empty"
    elif not object:
        name = "Fake"
    if object:
        print("Type not Found")
        return 1
    else:
        print(f"{name}: {object} {typeee}")
        return 0
