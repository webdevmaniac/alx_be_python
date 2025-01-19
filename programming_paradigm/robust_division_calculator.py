def safe_divide(numerator, denominator):
    """
    Perform division while handling errors like division by zero and non-numeric input.
    :param numerator: The numerator (can be string or numeric).
    :param denominator: The denominator (can be string or numeric).
    :return: Result of the division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."

# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command-line interactions for the division calculator.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
