from operations.base_operation import Operation


class AddOperation(Operation):
    def execute(self, numbers):
        # Check for negative numbers
        # Storing a list to return the negative values
        negative_numbers = [num for num in numbers if num < 0]
        if negative_numbers:
            return f"Negative numbers not allowed: {', '.join(map(str, negative_numbers))}"
        return sum(numbers)
