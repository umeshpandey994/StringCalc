from operations.base_operation import Operation


class MulOperation(Operation):
    def execute(self, numbers):
        result = 1
        for num in numbers:
            result *= num

        return result
