# Welcome message to introduce the program
print("Welcome to the Stress and Strain Calculator")
print("===========================================")

# Main program loop to allow for repeated calculations
while True:
    try:
        # Collecting user inputs
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

        # Outputting results with proper formatting
        print("\nResults:")
        print("---------")
        print(f"Stress: {stress:.2f} Pascals (Pa)")
        print(f"Strain: {strain:.6f} (dimensionless)")

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
        # Exiting message
        print("\nThank you for using the calculator. Goodbye!")
        break
