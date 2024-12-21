def is_nan(value):
    return value != value

def NULL_not_found(object: any) -> int:
    typeee = type(object)
    name = ""
    if object == None:
        name = "Nothing"
    elif is_nan(object):
        name = "Cheese"
        print(f"{name}: {object} {typeee}")
        return 0
    elif typeee.__name__ == "int" and object == 0:
        name = "Zero"
    elif object == '':
        name = "Empty"
    elif not object:
        name = "Fake"
    if object:
        print("Type not Found")
        return 1
    else:
        print(f"{name}: {object} {typeee}")
        return 0





# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(42)
# print(NULL_not_found("Brian"))