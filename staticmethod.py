class Calculator:

    @staticmethod
    def add_two_number(x, y):
        return x + y


# Calculator.add_two_number = staticmethod(Calculator.add_two_number)
print(Calculator.add_two_number(2, -5))