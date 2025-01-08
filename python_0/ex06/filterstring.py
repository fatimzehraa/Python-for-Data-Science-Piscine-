import argparse


class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise AssertionError("Bad args!")


# def valid_str(value):
#     if not all(char.isalnum() or char==' ' for char in value):
#         raise AssertionError("bad str")
#     return value


def main():
    """Filters words in a string by length."""
    try:
        valid_str = lambda value: (
            value
            if all(char.isalnum() or char == " " for char in value)
            else AssertionError("bad str")
        )
        parser = ThrowingArgumentParser()
        parser.add_argument("string", type=valid_str)
        parser.add_argument("integer", type=int)
        args = parser.parse_args()
        words = args.string.split(" ")
        result = [word for word in words if len(word) > args.integer]
        print(result)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
