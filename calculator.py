class Calculator:
    value: float

    def __init__(self):
        self.value = 0

    def adder(self, input1: float, input2: float) -> float:
        self.value = input1 + input2

    def subtractor(self, input1: float, input2: float) -> float:
        self.value = input1 - input2

    def multiplier(self, input1: float, input2: float) -> float:
        self.value = input1 * input2

    def divider(self, input1: float, input2: float) -> float:
        self.value = input1 / input2

    # Reset value to 0
    def clear(self) -> None:
        self.value = 0


# Get a float from user input
def get_float(prompt) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input!")
            continue
        # Valid input, exit loop
        else:
            break
    return value


def main() -> None:
    calc = Calculator()
    x: int = get_float("Enter a first input value for the calculator:\n")
    y: int = get_float("Enter a second input value for the calculator:\n")
    calc.adder(x, y)
    print("adder result: " + str(calc.value))
    calc.subtractor(x, y)
    print("subtractor result: " + str(calc.value))
    calc.multiplier(x, y)
    print("multiplier result: " + str(calc.value))
    calc.divider(x, y)
    print("divider result: " + str(calc.value))
    calc.clear()
    print("post calculator clear: " + str(calc.value))


if __name__ == '__main__':
    main()
