# Stage 1: Hard-coded variables for quadratic model
# Quadratic equation: y = ax^2 + bx + c

# Coefficients (hard-coded)
a = 2  # Represents the quadratic effect
b = 5  # Represents the linear effect
c = 3  # Represents the constant effect

# Independent variable (e.g., time in days)
x = 4  

# Calculate the weather prediction
y = a * (x**2) + b * x + c

# Display the results
print("Quadratic Weather Model")
print(f"Equation: y = {a}x^2 + {b}x + {c}")
print(f"Prediction for x = {x}: y = {y}")
