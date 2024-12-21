
import sys

#sys.tracebacklimit = 0

class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"

if len(sys.argv) == 1:
    exit()

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    try:
        argument = int(sys.argv[1])
        if argument % 2:
            print("I'm Odd")
        else:
            print("I'm Even")
    except ValueError:
        raise AssertionError("argument is not an integer") from None
except AssertionError as e:
    print(e)

