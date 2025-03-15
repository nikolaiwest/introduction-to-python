# Initialize an empty list to store history of calculations
calculations_history = []

# Set for unique materials (assuming each material has a unique identifier)
unique_materials = set()

# Tuple for units (immutable data)
units = ("Newtons", "Square Meters", "Pascals", "Meters", "Dimensionless")

# Welcome message
print("Welcome to the Enhanced Stress and Strain Calculator")
print("===========================================")

while True:
    try:
        # Collecting user inputs
        material_id = input("\nEnter material identifier (or type 'exit' to finish): ")
        if material_id.lower() == "exit":
            break

        # Add material to set of unique materials
        unique_materials.add(material_id)

        force = float(input("Enter the applied force (in newtons): "))
        area = float(input("Enter the cross-sectional area (in square meters): "))

        # Check for zero area to prevent division by zero
        if area == 0:
            print("Error: Area cannot be zero (division by zero)")
            continue

        original_length = float(
            input("Enter the original length of the material (in meters): ")
        )

        # Check for zero original length to prevent division by zero
        if original_length == 0:
            print("Error: Original length cannot be zero (division by zero)")
            continue

        change_in_length = float(
            input("Enter the change in length of the material (in meters): ")
        )

        # Calculating stress and strain
        stress = force / area  # Stress calculation
        strain = change_in_length / original_length  # Strain calculation

        # Store results in a dictionary
        result = {
            "Material ID": material_id,
            "Force (N)": force,
            "Area (m^2)": area,
            "Stress (Pa)": stress,
            "Original Length (m)": original_length,
            "Change in Length (m)": change_in_length,
            "Strain": strain,
        }

        # Add the result dictionary to the history list
        calculations_history.append(result)

        # Display current calculation
        print(f"\nMaterial ID: {material_id}")
        print(f"Calculated Stress: {stress:.2f} {units[2]}")
        print(f"Calculated Strain: {strain:.6f} {units[4]}")

        # Simple result interpretation
        if stress > 1000000:  # More than 1 MPa
            print("\nNote: The stress level is relatively high.")

    except ValueError:
        # Handling invalid numeric input
        print("Invalid input. Please enter a valid number.")
        continue

    except ZeroDivisionError:
        # This shouldn't be reached due to our earlier checks, but just in case
        print("Error: Cannot divide by zero. Area or original length must be non-zero.")

    # Asking the user if they want to perform another calculation
    repeat = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if repeat != "yes" and repeat != "y":
        break

# Displaying the session history and unique materials
if calculations_history:
    print("\n===========================================")
    print("Session Summary:")
    for calculation in calculations_history:
        print(calculation)

    print("\nUnique Materials Tested:")
    print(unique_materials)
else:
    print("\nNo calculations were performed in this session.")

print("\nThank you for using the calculator. Goodbye!")
