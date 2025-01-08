import argparse

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


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
    if not all(char.isalnum() or char == " " for char in value):
        raise AssertionError("bad str")
    return value


def main():
    """Encodes a string into morse code."""
    try:
        parser = ThrowingArgumentParser()
        parser.add_argument("string", type=valid_str)
        string = parser.parse_args().string
        array = [NESTED_MORSE[char] for char in string.upper()]
        result = " ".join(array)
        print(result)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
