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

def valid_str(value):
    for char in value:
        if not (char.isalnum() or char==' '):
            raise AssertionError("bad str")
    return value

def main():
    try:
        parser = ThrowingArgumentParser()
        parser.add_argument("string", valid_str)
        parser.add_argument("integer", type=int)
        args = parser.parse_args()
        print(args)
    except AssertionError as e:
        print(e)
    return(0)


if __name__ == "__main__":
    main()