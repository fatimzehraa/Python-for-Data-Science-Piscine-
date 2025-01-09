def all_thing_is_obj(object: any) -> int:
    typeee = type(object)
    if typeee.__name__ == "int":
        print("Type not found")
        return 42
    elif typeee.__name__ == "str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")

    return 42
