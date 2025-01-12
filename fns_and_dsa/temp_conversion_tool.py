# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main script
if __name__ == "__main__":
    try:
        # Prompt user for temperature input
        temperature = input("Enter the temperature to convert: ").strip()
        if not temperature.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temperature)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)
