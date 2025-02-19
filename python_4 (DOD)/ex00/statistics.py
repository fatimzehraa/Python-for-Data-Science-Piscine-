def ft_statistics(*args: any, **kwargs: any) -> None:
    """variadik function"""
    lst = list(args)
    if len(lst) > 1:
        mean = sum(lst) / len(lst)
        var = sum([(i - mean) ** 2 for i in lst]) / len(lst)
    for key, value in kwargs.items():
        if len(lst) == 0:
            print("ERROR")
            continue
        if value == "mean":
            print(f"{value} = {mean}")
        elif value == "median":
            print(f"{value} = {sorted(lst)[len(lst) // 2]}")
        elif value == "quartile":
            print(f"{value} = [{sorted(lst)[len(lst) // 4]}, {sorted(lst)[3 * len(lst) // 4]}]")
        elif value == "var":
            print(f"{value} = {var}")
        elif value == "std":
            print(f"{value} = {var ** 0.5}")
    

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")