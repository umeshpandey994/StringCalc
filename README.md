# String Calculator

This python code implements a String Calculator that takes a string of numbers and performs addition operations, using different delimiters. It supports custom and multiple delimiters

## Features

- **Addition**: Adds numbers in the string.
- **Custom Delimiters**: Supports passing custom delimiters as arguments (both single and multiple).
- **Negative Numbers Handling**: Raises an exception and returns an error message when negative numbers are encountered.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/umeshpandey994/StringCalc.git
   cd StringCalc

2. Create a virtual environment and install dependencies:
    ```bash
    pyenv virtualenv 3.11.4 string-calc3.11.4 
    pyenv activate string-calc
    pip install -r requirements.txt

3. Usage
You can use the calculator to perform operations on a string of numbers, either using the default delimiter (comma) or custom delimiters.
    ```
    from operations.calculator import Calculator
    calc = Calculator()
    
    # Default delimiter (comma)
    result = calc.calculate("1,2,3") # output: 6

    # Custom multiple delimiters
    result = calc.calculate("1;2&3", "add", delimiter=[";", "&"]) # output: 6
   
   # Handling negative numbers
   result = calc.calculate("1,-2,3")
   print(result)  # Output: "Negative numbers not allowed:[-2]"


4. Running Tests
The project uses pytest for unit testing. Run the following command to execute the tests:
    ```
    pytest
