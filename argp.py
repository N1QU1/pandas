import argparse
from webbrowser import open_new

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help= "First number")
    parser.add_argument("number2", help="Second number")
    parser.add_argument("operation", help="Operation")

    args = parser.parse_args()

    result = 0
    n1 = int(args.number1)
    n2 = int(args.number2)
    op = args.operation
    match op:
        case "+":
            result = n1 + n2
        case "-":
            result = n1 - n2


    print(str(result))


