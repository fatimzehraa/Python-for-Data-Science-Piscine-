import argparse

class AssertionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"AssertionError: {self.message}"
    
# class ArgumentParserError(Exception): pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise AssertionError("few args")

def get_line() -> str :
    try:
        parser = ThrowingArgumentParser(description="display the sums of a text's \
            upper-case characters, lower-case \
            characters, punctuation characters, digits and spaces.")
        parser.add_argument("text", help="the text to be counted")
        args, extra_args = parser.parse_known_args()
        if extra_args:
            raise AssertionError("Too much args, please put your text inside quotes!")
        text = args.text
        return text
    except AssertionError as e:
        print(e)
        exit()



def main():
    text = get_line()
    char = len(text)
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    punctuation_check = '!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~'
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        elif i in punctuation_check:
            punctuation += 1
    print(f"The text contains {char} characters:\n{upper} upper letters\n{lower} lower letters\
        \n{punctuation} punctuation marks\n{space} spaces\n{digit} digits")

if __name__ == "__main__":
    main()