from operations.base_operation import Operation


class AddOperation(Operation):
    def execute(self, numbers):
        return sum(numbers)
