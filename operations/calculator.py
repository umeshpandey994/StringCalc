from operations.add_operation import AddOperation
from operations.mul_operation import MulOperation
from operations.parser import StringParser


class Calculator:
    """
        base class to perform the arithmetic operations
    """
    def __init__(self):
        self.operations = {
            "add": AddOperation(),
            "mul": MulOperation(),
        }

    def calculate(
            self, input_string: str, operation_type: str = "add",
            delimiter: list = ","
    ):
        """
            This function will do the Arithmetic operations
            :param input_string: Input string
            :param operation_type: add, subtract, multiple default value is add
            :param delimiter: list of delimiters
            :return: Int or ValueError
        """
        if not input_string:
            return 0

        try:
            numbers = StringParser.parse_string(input_string, delimiter)
            negative_numbers = [num for num in numbers if num < 0]
            if negative_numbers:
                return f"Negative numbers not allowed: {', '.join(map(str, negative_numbers))}"

        except ValueError as e:
            return str(e)

        operation = self.operations.get(operation_type)
        print(numbers)
        if operation:
            return operation.execute(numbers)
        else:
            raise ValueError(f"Operation '{operation_type}' not supported")