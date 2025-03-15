# Stress and Strain Calculator

# Display a welcome message
print("Welcome to the Stress and Strain Calculator")
print("===========================================")

# Get user inputs and convert them to the appropriate data types
# Force and Area for stress calculation
force = float(input("Enter the applied force (in newtons): "))
area = float(input("Enter the cross-sectional area (in square meters): "))

# Original length and change in length for strain calculation
original_length = float(
    input("Enter the original length of the material (in meters): ")
)
change_in_length = float(
    input("Enter the change in length of the material (in meters): ")
)

# Calculate stress and strain
stress = force / area
strain = change_in_length / original_length

# Display the results with formatting
print("\nResults:")
print("---------")
print(f"Stress: {stress:.2f} Pascals (Pa)")
print(f"Strain: {strain:.6f} (dimensionless)")

# Optional: Display interpretations based on results
if stress > 1000000:  # More than 1 MPa
    print("\nNote: The stress level is relatively high.")
else:
    print("\nNote: The stress level is within typical ranges.")

print("\nThank you for using the Stress and Strain Calculator!")
