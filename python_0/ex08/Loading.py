BLOCK_CHAR = "▉"

def ft_tqdm(lst: range) -> None:
    """Prints a progress bar for a given iterable."""

    for i, element in enumerate(lst, 1):
        yield element
        prct = int(i / len(lst) * 100)
        bar = BLOCK_CHAR * prct + " " * (100 - prct)
        print(f"\r{prct}%|{bar}| {i}/{len(lst)}", end=" ")