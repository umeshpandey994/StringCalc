from operations.add_operation import AddOperation


class Calculator:
    """
        base class to perform the arithmetic operations
    """
    def __init__(self):
        self.operations = {
            'add': AddOperation()
        }

    def calculate(
            self, input_string: str, operation_type: str = "add"
    ):
        """
            This function will do the Arithmetic operations
            :param input_string: Input string
            :param operation_type: add, subtract, multiple default value is add
            :return: Int or ValueError
        """
        if not input_string:
            return 0

        try:
            numbers = [int(_) for _ in input_string.strip().split(",")]
        except ValueError as e:
            return str(e)

        operation = self.operations.get(operation_type)
        print(numbers)
        if operation:
            return operation.execute(numbers)
        else:
            raise ValueError(f"Operation '{operation_type}' not supported")