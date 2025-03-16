import numpy as np

# Define the conversion function
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# Vectorize the function
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

# Array of temperatures in Fahrenheit
fahrenheit_temps = np.array([32, 68, 100, 212, 77])

# Convert to Celsius
celsius_temps = vectorized_conversion(fahrenheit_temps)

# Display results
print(celsius_temps)