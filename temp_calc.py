"""
  Temperature Converter
  Converts temperatures between Celsius and Fahrenheit.
  Usage: Run the script and enter a temperature like 74F or 25C.
  """

temperature_response = input("Enter a temperature(C/F): ")
# Strip the response to the number and convert to float
temperature_number = float(temperature_response[0:-1])
# Normalize to uppercase to handle both 'f' and 'F'
temperature_letter = temperature_response[-1].upper()

if temperature_letter == "F":
    celcius_number = (temperature_number * 5 - 160) / 9
    print(f"{temperature_number}{temperature_letter} is {celcius_number:.1f}C")
elif temperature_letter == "C":
    fahrenheit_number = (temperature_number * 9 + 32 * 5 ) / 5
    print(f"{temperature_number}{temperature_letter} is {fahrenheit_number:.1f}F")
else:
    print("Usage: 74F or 25C")
