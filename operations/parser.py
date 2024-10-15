import re


class StringParser:
    @staticmethod
    def parse_string(input_string, delimiters=None):
        # Handle delimiters
        if isinstance(delimiters, list):
            delimiters = [re.escape(d) for d in delimiters]
            delimiters_pattern = "|".join(delimiters)
        else:
            delimiters_pattern = re.escape(delimiters)

        # Split the input string based on the delimiters
        numbers = re.split(delimiters_pattern, input_string)
        parsed_numbers = [int(num) for num in numbers if num]

        return parsed_numbers
