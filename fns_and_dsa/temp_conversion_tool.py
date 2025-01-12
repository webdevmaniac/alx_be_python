# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    try:
        # Prompt the user for temperature input
        temperature_input = input("Enter the temperature to convert: ")
        
        # Validate numeric input
        try:
            temperature = float(temperature_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Prompt the user for the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the appropriate conversion
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temp:.2f}°F")
        else:
            print("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()