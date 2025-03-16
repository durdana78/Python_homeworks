import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 - 4*x + 4

# Generate x values using a list comprehension
x_values = [x / 10 for x in range(-100, 101)]  # Creating x values from -10 to 10 with small steps
y_values = [f(x) for x in x_values]  # Compute corresponding y values

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label=r'$f(x) = x^2 - 4x + 4$', color='blue')

# Customize the plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function $f(x) = x^2 - 4x + 4$')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()