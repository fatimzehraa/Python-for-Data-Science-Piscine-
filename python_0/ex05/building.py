import argparse
import sys


class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"


def get_line() -> str:
    """get_line(): parses text to be counted as argument using argparse,\
        and throws AssertionError if more than one argument is provided."""
    try:
        parser = argparse.ArgumentParser(description="parse args")
        parser.add_argument("text", nargs="?", help="the text to be counted")
        args, extra_args = parser.parse_known_args()
        text = args.text
        if extra_args:
            raise AssertionError(
                "Too much args, please put your text\
                inside quotes!"
            )
        return text
    except AssertionError as e:
        print(e)
        exit()


def main():
    """This program tends to count and display the sums of upper/lower
    case characters, punctuations, digits, and spaces in user input."""
    text = get_line()
    if text is None:
        print("What is the text to count?")
        text = sys.stdin.read()
    char = len(text)
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    punctuation_check = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():  # or i == '\n':
            space += 1
        elif i.isdigit():
            digit += 1
        elif i in punctuation_check:
            punctuation += 1
    print(
        f"The text contains {char} characters:\n{upper} upper letters\n\
{lower} lower letters\n{punctuation} punctuation marks\n\
{space} spaces\n{digit} digits"
    )


if __name__ == "__main__":
    main()
